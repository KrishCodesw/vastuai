from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .rule_engine import load_rules, apply_combined_rules, generate_report_string  # import logic
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
vastu_path = os.path.join(base_dir, "IndianVastuRuleBase.json")
fengshui_path = os.path.join(base_dir, "ChineseVastuRuleBase.json")

@csrf_exempt
def vastu_analysis_view(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            mode = body.get("mode", "hybrid").lower()
            test_input = body.get("test_input", {})

            if mode not in ["vastu", "fengshui", "hybrid"]:
                return JsonResponse({"error": "Invalid mode"}, status=400)

            vastu_rules, fengshui_rules = load_rules(vastu_path, fengshui_path)
            result = apply_combined_rules(test_input, mode, vastu_rules, fengshui_rules)
            report = generate_report_string(result, mode, test_input)

            return JsonResponse({"report": report})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST allowed"}, status=405)






