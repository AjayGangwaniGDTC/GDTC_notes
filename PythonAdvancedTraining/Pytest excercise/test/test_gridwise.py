from datetime import datetime, timedelta
from gridwise import gridwise_engine
import pytest

def test_grid_node_initialisation():
    node = gridwise_engine.GridNode(1)
    assert node.voltage==1.0
    
def test_voltage_range():
    node = gridwise_engine.GridNode(2)
    assert node.is_voltage_safe() is True
    
def test_detect_unsafe_overvoltage():
    node = gridwise_engine.GridNode(3)
    node.update_voltage(1.08)
    assert node.is_voltage_safe() is False
    
def test_detect_unsafe_undervoltage():
    node = gridwise_engine.GridNode(3)
    node.update_voltage(0.91)
    assert node.is_voltage_safe() is False
    
def test_allow_manual_override():
    node = gridwise_engine.GridNode(4)
    five_minutes_before = datetime.utcnow() - timedelta(minutes=6)
    node.last_override = five_minutes_before
    now = datetime.utcnow()
    assert node.trigger_override(now) is True
    
def test_block_override_if_cooldown_not_passed():
    node = gridwise_engine.GridNode(5)
    five_minutes_before = datetime.utcnow() - timedelta(minutes=3)
    node.last_override = five_minutes_before
    now = datetime.utcnow()
    assert node.trigger_override(now) is False
    
def test_log_power_usage():
    tracker = gridwise_engine.EnergyTracker()
    now = datetime.utcnow()
    tracker.log_usage(now, 4.56)
    assert len(tracker.power_data) == 1
    
def test_30_min_average():
    tracker = gridwise_engine.EnergyTracker()
    now = datetime.utcnow()
    tracker.log_usage(now-timedelta(minutes=25), 5.4)
    tracker.log_usage(now-timedelta(minutes=20), 2.36)
    tracker.log_usage(now-timedelta(minutes=10), 8.46)
    tracker.log_usage(now, 6.64)
    avg = tracker.get_average_load()
    assert avg == 5.715
    
def test_handle_no_data_safely():
    tracker = gridwise_engine.EnergyTracker()
    assert tracker.get_average_load()==0
    
def test_end_to_end_override_and_safety():
    node = gridwise_engine.GridNode(6)
    node.update_voltage(1.08)
    assert node.is_voltage_safe() is False
    now = datetime.utcnow()
    assert node.trigger_override(now) is True
        