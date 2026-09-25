import { api } from './api';

export const createTicket = (payload) => api.post('/tickets', payload);
export const getTicket = (ticketId) => api.get(`/tickets/${ticketId}`);
export const getMyTickets = (email) => api.get('/tickets', { params: email ? { search: email } : {} });
export const updateTicket = (ticketId, payload) => api.put(`/tickets/${ticketId}`, payload);
export const addComment = (ticketId, payload) => api.post(`/tickets/${ticketId}/comments`, payload);
export const uploadAttachment = (ticketId, file) => {
  const data = new FormData();
  data.append('file', file);
  return api.post(`/tickets/${ticketId}/attachments`, data, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
};
export const closeTicket = (ticketId, performedBy) => updateTicket(ticketId, { status: 'Closed', performed_by: performedBy });
export const reopenTicket = (ticketId, performedBy) => updateTicket(ticketId, { status: 'Open', performed_by: performedBy });
