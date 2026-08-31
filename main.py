# AI Task Risk & Priority Classifier
# Task 1 Submission

import re

def analyze_task_risk(task_description):
    """
    Analyzes project task descriptions and assigns a risk/priority level.
    """
    task_lower = task_description.lower()
    
    # High-risk trigger keywords
    high_risk_keywords = ['crash', 'breach', 'bug', 'failure', 'downtime', 'delayed', 'security']
    
    # Check for keywords
    if any(keyword in task_lower for keyword in high_risk_keywords):
        return "HIGH RISK (Immediate Action Required)"
    else:
        return "LOW RISK (Standard Workflow)"

# Test Dataset
sample_tasks = [
    "System server crash blocking project deployment",
    "Update weekly team slide deck format",
    "Security breach identified in main database",
    "Schedule routine sync call with client",
    "API integration failure causing checkout errors"
]

print("--- AI PROJECT RISK & PRIORITY ANALYSIS ---")
for idx, task in enumerate(sample_tasks, 1):
    risk_level = analyze_task_risk(task)
    print(f"\nTask {idx}: {task}")
    print(f"Status: {risk_level}")
