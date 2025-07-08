import json
import sys

def load_rules(vastu_path, fengshui_path):
    with open(vastu_path, 'r', encoding='utf-8') as vfile, open(fengshui_path, 'r', encoding='utf-8') as ffile:
        vastu_rules = json.load(vfile)
        fengshui_rules = json.load(ffile)
    return vastu_rules, fengshui_rules

def evaluate_conditions(rule_conditions, input_facts):
    for condition in rule_conditions:
        fact = condition["fact"]
        expected_value = condition["value"]
        operator = condition.get("operator", "equals")
        fact_value = input_facts.get(fact)

        if operator == "equals" and fact_value != expected_value:
            return False
        elif operator == "not_equals" and fact_value == expected_value:
            return False
        elif operator == "in" and fact_value not in expected_value:
            return False
    return True

def apply_rule_set(rules, input_facts, active_system):
    positives = []
    negatives = []
    score = 0

    system_map = {
        "indian vastu": "vastu",
        "vastu": "vastu",
        "chinese feng shui": "fengshui",
        "feng shui": "fengshui",
        "fengshui": "fengshui"
    }

    for rule in rules:
        normalized_system = system_map.get(rule["system"].lower().strip(), rule["system"].lower().strip())

        if active_system != "hybrid" and normalized_system != active_system:
            continue

        if evaluate_conditions(rule["conditions"], input_facts):
            result = {
                "system": rule["system"],
                "name": rule["name"],
                "tip": rule["consequence"].get("short_message", "Not provided"),
                "description": rule.get("description") or rule["consequence"].get("description", "Not provided"),
                "consequence": rule["consequence"].get("message", "Not provided"),
                "remedy": rule["remedy"].get("description", "Not provided"),
                "severity": rule["consequence"].get("severity", "Not provided").capitalize(),
                "source": rule.get("source_reference", "Not provided"),
                "type": rule["consequence"]["type"]
            }

            if rule["consequence"]["type"] == "favorable":
                positives.append(result)
            else:
                negatives.append(result)

            score += rule["compatibility"].get("indian_vastu_score", 0)
            score += rule["compatibility"].get("feng_shui_score", 0)

    return positives, negatives, score

def apply_combined_rules(input_facts, rule_mode, vastu_rules, fengshui_rules):
    total_score = 50  # neutral starting point
    all_rules = []

    if rule_mode == "vastu":
        all_rules = vastu_rules
    elif rule_mode == "fengshui":
        all_rules = fengshui_rules
    elif rule_mode == "hybrid":
        all_rules = vastu_rules + fengshui_rules
    else:
        raise ValueError("Invalid rule mode. Use 'vastu', 'fengshui', or 'hybrid'.")

    positives, negatives, score = apply_rule_set(all_rules, input_facts, rule_mode)
    total_score += score * 10
    total_score = max(0, min(100, total_score))

    return {
        "score": total_score,
        "positives": positives,
        "negatives": negatives
    }

def print_report(result, mode):
    print("=" * 60)
    print(f"VASTU INTELLIGENCE REPORT".ljust(45) + f"Mode: {mode.upper()}")
    print("=" * 60)
    print(f"Overall Compatibility Score: {result['score']}/100\n")
    
    if test_input:
        print("TEST INPUT SNAPSHOT")
        print("-" * 60)
        for key, value in test_input.items():
            print(f"{key.ljust(30)}: {value}")
        print()

    

    if result['positives']:
        print("POSITIVE OBSERVATIONS")
        print("-" * 60)
        for i, item in enumerate(result['positives'], 1):
            print(f"[{i}] {item['name']} — {item['system']} ({item['severity']})")
            print(f"    Tip         : {item['tip']}")
            print(f"    Description : {item['description']}")
            print(f"    Consequence : {item['consequence']}")
            print(f"    Remedy      : {item['remedy']}")
            print(f"    Source      : {item['source']}\n")
    else:
        print("POSITIVE OBSERVATIONS")
        print("    None found.\n")

    if result['negatives']:
        print("NEGATIVE FINDINGS")
        print("-" * 60)
        for i, item in enumerate(result['negatives'], 1):
            print(f"[{i}] {item['name']} — {item['system']} ({item['severity']})")
            print(f"    Tip         : {item['tip']}")
            print(f"    Description : {item['description']}")
            print(f"    Consequence : {item['consequence']}")
            print(f"    Remedy      : {item['remedy']}")
            print(f"    Source      : {item['source']}\n")
    else:
        print("NEGATIVE FINDINGS")
        print("    No defects or warnings detected.\n")

    print("=" * 60 + "\n")

if __name__ == "__main__":
    try:
        mode = sys.argv[1].lower()
    except IndexError:
        mode = input("Enter analysis mode (vastu / fengshui / hybrid): ").strip().lower()

    if mode not in ["vastu", "fengshui", "hybrid"]:
        print("Invalid mode. Please use one of: vastu / fengshui / hybrid")
        sys.exit(1)

    vastu_rules, fengshui_rules = load_rules("IndianVastuRuleBase.json", "ChineseVastuRuleBase.json")

    # test_input = {
    #    "room.room_type": "entrance",
    # "room.facing_direction": "Southwest",
    # "object.object_type": "stove",
    # "object.facing_direction": "North",  # irrelevant here
    # "object.metadata.is_fire_element": True,
    # "object_reflects_bed": False
    # } 
    # This is the test input which will come dynamically and fill in 
    test_input = {
      "room.room_type": "kitchen",
    "room.room_center_direction": "Northwest",
    "object.object_type": "stove",
    "object.facing_direction": "South",
    "object.metadata.is_fire_element": True,
    "object_reflects_bed": False
}


    result = apply_combined_rules(test_input, mode, vastu_rules, fengshui_rules)
    print_report(result, mode)
