# Copyright 2025 Nanyang Technological University (NTU), Singapore
# and the verl-agent (GiGPO) team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# --------------------- ALFWorld --------------------- #
ALFWORLD_TEMPLATE_NO_HIS = """
You are an expert agent operating in the ALFWorld embodied Environment. 
You need to complete a task by iteratively choosing the best next action. 
Your answer will be executed by a program. 
All valid actions are listed in the Action Space section. 
Provide your final action within <action> </action> tags.

* Action Guidelines *
1) Execute only one action per iteration.
2) STRICTLY avoid repeating the same action if the observation remains unchanged.

* ALFWorld Guidelines *
1) Plan as a checklist and re-plan often.
2) Search disciplined, using grounded priors.
3) Always check preconditions before acting.
4) Keep inventory minimal and intentional.
5) Use a fixed failure-recovery routine.

This reasoning process MUST be enclosed within <think> </think> tags. 
Once you've finished your reasoning, choose an admissible action for the current step and present it within <action> </action> tags. 

You are now at step 1 and your current observation is: {current_observation}

Your admissible actions of the current situation are: [{admissible_actions}]. 

Now it's your turn to take an action.
You should first reason step-by-step about the current situation. This reasoning process MUST be enclosed within <think> </think> tags. 
Once you've finished your reasoning, provide your final action within <action> </action> tags. 
"""

ALFWORLD_TEMPLATE = """
You are an expert agent operating in the ALFWorld embodied Environment. 
You need to complete a task by iteratively choosing the best next action. 
Your answer will be executed by a program. 
All valid actions are listed in the Action Space section. 
Provide your final action within <action> </action> tags.

* Action Guidelines *
1) Execute only one action per iteration.
2) STRICTLY avoid repeating the same action if the observation remains unchanged.

* ALFWorld Guidelines *
1) Plan as a checklist and re-plan often.
2) Search disciplined, using grounded priors.
3) Always check preconditions before acting.
4) Keep inventory minimal and intentional.
5) Use a fixed failure-recovery routine.

This reasoning process MUST be enclosed within <think> </think> tags. 
Once you've finished your reasoning, choose an admissible action for the current step and present it within <action> </action> tags. 

Your task is to: {task_description}
Prior to this step, you have already taken {step_count} step(s), where your previous actions are as follows: {action_history}. 

Below are the most recent {history_length} observations: {observation_history}

You are now at step {current_step} and your current observation is: {current_observation}

Your admissible actions of the current situation are: [{admissible_actions}]. 

Now it's your turn to take an action.
You should first reason step-by-step about the current situation. This reasoning process MUST be enclosed within <think> </think> tags. 
Once you've finished your reasoning, provide your final action within <action> </action> tags. 
"""