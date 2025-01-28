from odoo import models, fields
from odoo.exceptions import UserError

class project_task(models.Model):
    _inherit = ['project.task']

    x_task_type = fields.Selection(
        selection=[
            ('01_new_development', 'New development'),
            ('02_bug_fixing', 'Bug Fixing')], 
        string="Task Type")
    
    x_task_category = fields.Selection(
        selection=[
            ('01_crim', 'CRIM'),
            ('02_report', 'Report')], 
        string="Task Category")
    
    bug_id = fields.Char(string="Bug ID")

    bug_type = fields.Selection(
        selection=[
            ('01_technical', 'Technical'),
            ('02_functional', 'Functional'),
            ('03_non_functional', 'Non-Functional')], 
        string="Bug Type")

    date_start = fields.Date(string='Start Date')

    jira_id = fields.Char(string="JIRA ID")

    complete_percentage = fields.Char(string="Completion Percentage")

    spoc = fields.Char(string="Functional SPOC")

    assigned_date = fields.Date(string='Assigned Date')

    revised_edc = fields.Date(string='Revised EDC')

    remarks = fields.Text(string="Remarks")

    edc = fields.Date(string="EDC")

    def write(self, vals):
        # Check if the stage_id is being updated
        if 'stage_id' in vals:
            # Get the Project User and Project Manager groups
            project_user_group = self.env.ref('project.group_project_user')
            project_manager_group = self.env.ref('project.group_project_manager')

            for task in self:
                new_stage = self.env['project.task.type'].browse(vals['stage_id']).name
                new_stage_seq = self.env['project.task.type'].browse(vals['stage_id']).sequence
                    # Check if the new stage is "Estimation"
                if new_stage == 'Estimation':
                    if task.bug_type in ['01_technical', '03_non_functional']:
                        raise UserError(
                            f"Tasks with Bug Type '{dict(task._fields['bug_type'].selection).get(task.bug_type)}' "
                                    "cannot be moved to the 'Estimation' stage."
                        )
                      
            # for task in self:
            #     new_stage_seq = self.env['project.task.type'].browse(vals['stage_id']).sequence
                # Ensure that the state is "Approved" before moving to the next stage
                if task.state != '03_approved' and new_stage_seq > task.stage_id.sequence:
                    raise UserError(
                        f"Task cannot be moved to the next stage unless the state is set to 'Approved'."
                    )
                
            # Check if the user is in Project User group and not in Project Manager group
            if project_user_group in self.env.user.groups_id and project_manager_group not in self.env.user.groups_id:
                for task in self:
                    old_stage_seq = task.stage_id.sequence
                    old_stage = task.stage_id.name
                    new_stage = self.env['project.task.type'].browse(vals['stage_id']).name
                    new_stage_seq = self.env['project.task.type'].browse(vals['stage_id']).sequence

                    # Add your custom warning condition
                    if old_stage_seq > new_stage_seq:  # Example: Warning for any stage change
                        raise UserError(f"As a Project User, you cannot move the task from '{old_stage}' to '{new_stage}'.")
                    elif new_stage_seq > old_stage_seq + 1:  # Example: Warning for any stage change
                        if new_stage == 'Development' and old_stage == 'FS Clarification' and task.bug_type in ['01_technical', '03_non_functional']:
                            pass
                        else:
                            raise UserError(f"As a Project User, you cannot move the task more than one stage.")
            
                
        
        return super(project_task, self).write(vals)
