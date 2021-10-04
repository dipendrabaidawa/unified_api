from dataclasses import dataclass

@dataclass
class TodoistNewProject():

     task_id: str = None
     section_id: str = None
     event_data: str = None
     child_order: str = None
     collapsed: str = None
     color: str = None
     id: str = None
     is_archived: str = None
     is_deleted: str = None
     is_favorite: str = None
     name: str = None
     parent_id: str = None
     shared: str = None
     sync_id: str = None
     event_name: str = None
     initiator: str = None
     email: str = None
     full_name: str = None
     image_id: str = None
     user_id: str = None
     version: str = None