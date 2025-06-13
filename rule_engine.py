import json

def load_rules(vastu_path, fengshui_path):
    with open(vastu_path, 'r') as vfile, open(fengshui_path, 'r') as ffile:
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
    return True

def apply_rule_set(rules, input_facts, active_system):
    suggestions = []
    score = 0

    for rule in rules:
        if active_system != "hybrid" and rule["system"].lower() != active_system:
            continue
        if evaluate_conditions(rule["conditions"], input_facts):
            msg = rule["consequence"].get("short_message", rule["name"])
            suggestions.append(f"{rule['system']}: {msg}")
            score += rule["compatibility"].get("indian_vastu_score", 0)
            score += rule["compatibility"].get("feng_shui_score", 0)
    return suggestions, score

def apply_combined_rules(input_facts, rule_mode, vastu_rules, fengshui_rules):
    suggestions = []
    total_score = 50  # neutral base

    all_rules = []
    if rule_mode == "vastu":
        all_rules = vastu_rules
    elif rule_mode == "fengshui":
        all_rules = fengshui_rules
    elif rule_mode == "hybrid":
        all_rules = vastu_rules + fengshui_rules
    else:
        raise ValueError("Invalid rule mode")

    matched_suggestions, score = apply_rule_set(all_rules, input_facts, rule_mode)
    suggestions.extend(matched_suggestions)
    total_score += score * 10  # scale scoring
    total_score = max(0, min(100, total_score))

    return {
        "score": total_score,
        "suggestions": suggestions
    }

# Example usage
if __name__ == "__main__":
    vastu, fengshui = load_rules("IndianVastuRuleBase.json", "ChineseVastuRuleBase.json")

    test_input = {
        "room.room_type": "kitchen",
        "room.room_center_direction": "Northeast",
        "object.object_type": "stove",
        "object.facing_direction": "East",
        "object.metadata.is_fire_element": True,
        "object_reflects_bed": False
    }

    for mode in ["vastu", "fengshui", "hybrid"]:
        print(f"\n--- {mode.upper()} MODE ---")
        result = apply_combined_rules(test_input, mode, vastu, fengshui)
        print("Vastu Score:", result["score"])
        for s in result["suggestions"]:
            print("-", s)
