[
  {
    "rule_id": "IV_RM_KITCHEN_NE_001",
    "name": "Kitchen in Northeast Corner (Vastu Defect)",
    "description": "...",
    "system": "Indian Vastu",
    "category": "Room Placement",
    "target_entity": "Room",
    "target_type": "kitchen",
    "conditions": [
      { "fact": "room.room_type", "operator": "equals", "value": "kitchen" },
      { "fact": "room.room_center_direction", "operator": "equals", "value": "Northeast" }
    ],
    "consequence": {
      "type": "defect",
      "severity": "high",
      "message": "...",
      "short_message": "1500 Rs kaa daan kare"
    },
    "remedy": { "type": "general", "description": "..." },
    "compatibility": { "indian_vastu_score": 1, "feng_shui_score": 0 },
    "source_reference": "Agni Purana, Mayamatam"
  },
  {
    "rule_id": "IV_OBJ_STOVE_EAST_003",
    "name": "Stove Facing East (Favorable)",
    "description": "...",
    "system": "Indian Vastu",
    "category": "Object Placement",
    "target_entity": "Object",
    "target_type": "stove",
    "conditions": [
      { "fact": "room.room_type", "operator": "equals", "value": "kitchen" },
      { "fact": "object.object_type", "operator": "equals", "value": "stove" },
      { "fact": "object.facing_direction", "operator": "equals", "value": "East" }
    ],
    "consequence": {
      "type": "favorable",
      "severity": "medium",
      "message": "...",
      "short_message": "..."
    },
    "remedy": { "type": "none", "description": "..." },
    "compatibility": { "indian_vastu_score": 1, "feng_shui_score": 0 },
    "source_reference": "Vastu principles for kitchen"
  },
  {
    "rule_id": "IV_RM_KITCHEN_SE_002",
    "name": "Kitchen in Southeast (Favorable)",
    "description": "Southeast is governed by Agni (fire), making it the ideal place for the kitchen, enhancing health and well-being.",
    "system": "Indian Vastu",
    "category": "Room Placement",
    "target_entity": "Room",
    "target_type": "kitchen",
    "conditions": [
      { "fact": "room.room_type", "operator": "equals", "value": "kitchen" },
      { "fact": "room.room_center_direction", "operator": "equals", "value": "Southeast" }
    ],
    "consequence": {
      "type": "favorable",
      "severity": "high",
      "message": "Kitchen in Southeast enhances digestive fire and health.",
      "short_message": "Excellent kitchen placement"
    },
    "remedy": { "type": "none", "description": "No remedy required." },
    "compatibility": { "indian_vastu_score": 1, "feng_shui_score": 1 },
    "source_reference": "Mayamatam, Vastu Vidya"
  },
  {
    "rule_id": "IV_RM_KITCHEN_NW_003",
    "name": "Kitchen in Northwest (Moderately Favorable)",
    "description": "A kitchen in the Northwest is acceptable, particularly when Southeast is unavailable, but it may lead to inconsistent food habits.",
    "system": "Indian Vastu",
    "category": "Room Placement",
    "target_entity": "Room",
    "target_type": "kitchen",
    "conditions": [
      { "fact": "room.room_type", "operator": "equals", "value": "kitchen" },
      { "fact": "room.room_center_direction", "operator": "equals", "value": "Northwest" }
    ],
    "consequence": {
      "type": "neutral",
      "severity": "medium",
      "message": "Kitchen in Northwest is permissible but may cause instability in domestic routines.",
      "short_message": "Manageable with care"
    },
    "remedy": {
      "type": "general",
      "description": "Use light yellow or white tones; maintain kitchen hygiene strictly."
    },
    "compatibility": { "indian_vastu_score": 0.7, "feng_shui_score": 0.5 },
    "source_reference": "Agni Purana, Manasara"
  },
  {
    "rule_id": "IV_RM_MBR_SW_004",
    "name": "Master Bedroom in Southwest (Favorable)",
    "description": "The southwest direction signifies strength and stability, making it ideal for the master bedroom to ensure authority and harmony.",
    "system": "Indian Vastu",
    "category": "Room Placement",
    "target_entity": "Room",
    "target_type": "master_bedroom",
    "conditions": [
      { "fact": "room.room_type", "operator": "equals", "value": "master_bedroom" },
      { "fact": "room.room_center_direction", "operator": "equals", "value": "Southwest" }
    ],
    "consequence": {
      "type": "favorable",
      "severity": "high",
      "message": "Master bedroom in the Southwest provides authority and stability in relationships.",
      "short_message": "Strong and favorable placement"
    },
    "remedy": { "type": "none", "description": "No remedy needed." },
    "compatibility": { "indian_vastu_score": 1, "feng_shui_score": 1 },
    "source_reference": "Samarangana Sutradhara, Vastu Vidya"
  },
