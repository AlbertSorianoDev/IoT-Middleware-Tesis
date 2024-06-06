from src.core.device_manager.equipment_control import EquipmentControl


class EquipmentService:
    def __init__(self):
        self.equipment_control = EquipmentControl()

    def get_equipment_by_id(self, equipment_id: int):
        equipment = self.equipment_control.get_equipment_by_id(equipment_id)

        if equipment:
            return equipment.to_dict()

        return None

    def get_equipments(self):
        return [
            equipment.to_dict()
            for equipment in self.equipment_control.equipments_index.values()
        ]

    def create_equipment(self, label: str, description: str):
        equipement = self.equipment_control.create_equipment(label, description)

        if equipement:
            return equipement.to_dict()

        return None
