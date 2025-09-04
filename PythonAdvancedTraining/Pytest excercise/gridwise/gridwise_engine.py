from datetime import datetime, timedelta

class GridNode:
    def __init__(self, node_id, max_voltage=1.05, min_voltage=0.95):
        self.node_id = node_id
        self.voltage = 1.00
        self.max_voltage = max_voltage
        self.min_voltage = min_voltage
        self.last_override = None

    def update_voltage(self, new_voltage):
        self.voltage = new_voltage

    def is_voltage_safe(self):
        return self.min_voltage <= self.voltage <= self.max_voltage

    def trigger_override(self, current_time):
        if not self.last_override or (current_time - self.last_override) >= timedelta(minutes=5):
            self.last_override = current_time
            return True
        return False


class EnergyTracker:
    def __init__(self):
        self.power_data = []

    def log_usage(self, timestamp, load_kw):
        self.power_data.append((timestamp, load_kw))

    def get_average_load(self, minutes=30):
        now = datetime.utcnow()
        recent = [load for time, load in self.power_data if now - time <= timedelta(minutes=minutes)]
        return sum(recent) / len(recent) if recent else 0