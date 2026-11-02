from datetime import datetime
from app import db


class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_by = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(80), nullable=True)
    predicted_category = db.Column(db.String(80), nullable=True)
    category_confidence = db.Column(db.Float, default=0.0)
    priority = db.Column(db.String(40), default='Medium')
    priority_confidence = db.Column(db.Float, default=0.0)
    status = db.Column(db.String(40), default='Open')
    assigned_team_id = db.Column(db.Integer, nullable=True)
    assigned_agent_id = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    resolved_at = db.Column(db.DateTime, nullable=True)
    sla_deadline = db.Column(db.DateTime, nullable=True)
    ai_analysis = db.Column(db.Text, nullable=True)
    routing_reason = db.Column(db.Text, nullable=True)
    resolution_suggestions = db.Column(db.Text, nullable=True)
    department = db.Column(db.String(120), nullable=True)
    device = db.Column(db.String(120), nullable=True)
    location = db.Column(db.String(120), nullable=True)
    additional_info = db.Column(db.Text, nullable=True)
    error_message = db.Column(db.Text, nullable=True)
    email = db.Column(db.String(150), nullable=True)
    affected_users = db.Column(db.Integer, default=1)
    business_impact = db.Column(db.String(80), default='Low')
    downtime = db.Column(db.String(80), default='None')
    user_selected_category = db.Column(db.String(80), nullable=True)
    affected_users_range = db.Column(db.String(40), nullable=True)
    work_blocked = db.Column(db.Boolean, default=False)
    blocked_activity = db.Column(db.String(255), nullable=True)
    security_impact = db.Column(db.String(40), nullable=True)
    security_details = db.Column(db.Text, nullable=True)
    system_criticality = db.Column(db.String(80), nullable=True)
    started_at = db.Column(db.String(80), nullable=True)
    deadline = db.Column(db.String(80), nullable=True)
    user_reported_urgency = db.Column(db.String(40), nullable=True)

    # Relationships
    history = db.relationship('TicketHistory', backref='ticket', cascade='all, delete-orphan', lazy='dynamic')
    comments = db.relationship('Comment', backref='ticket', cascade='all, delete-orphan', lazy='dynamic')
    predictions = db.relationship('TicketPrediction', backref='ticket', cascade='all, delete-orphan', lazy='dynamic')
    attachments = db.relationship('Attachment', backref='ticket', cascade='all, delete-orphan', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_by': self.created_by,
            'category': self.category,
            'predicted_category': self.predicted_category,
            'category_confidence': round(self.category_confidence or 0.0, 4),
            'priority': self.priority,
            'priority_confidence': round(self.priority_confidence or 0.0, 4),
            'status': self.status,
            'assigned_team_id': self.assigned_team_id,
            'assigned_agent_id': self.assigned_agent_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'resolved_at': self.resolved_at.isoformat() if self.resolved_at else None,
            'sla_deadline': self.sla_deadline.isoformat() if self.sla_deadline else None,
            'ai_analysis': self.ai_analysis,
            'routing_reason': self.routing_reason,
            'resolution_suggestions': self.resolution_suggestions,
            'department': self.department,
            'device': self.device,
            'location': self.location,
            'additional_info': self.additional_info,
            'error_message': self.error_message,
            'email': self.email,
            'affected_users': self.affected_users,
            'business_impact': self.business_impact,
            'downtime': self.downtime,
            'user_selected_category': self.user_selected_category,
            'affected_users_range': self.affected_users_range,
            'work_blocked': self.work_blocked,
            'blocked_activity': self.blocked_activity,
            'security_impact': self.security_impact,
            'security_details': self.security_details,
            'system_criticality': self.system_criticality,
            'started_at': self.started_at,
            'deadline': self.deadline,
            'user_reported_urgency': self.user_reported_urgency,
        }
