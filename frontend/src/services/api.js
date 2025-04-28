import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const createStory = async (formData) => {
  const response = await api.post('/stories', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  return response.data;
};

export const getStory = async (id) => {
  const response = await api.get(`/stories/${id}`);
  return response.data;
};

export const downloadPdf = async (id) => {
  const response = await api.get(`/stories/${id}/pdf`, {
    responseType: 'blob',
  });
  
  const url = window.URL.createObjectURL(new Blob([response.data]));
  const link = document.createElement('a');
  link.href = url;
  link.setAttribute('download', `fairytale-${id}.pdf`);
  document.body.appendChild(link);
  link.click();
  link.remove();
};

export default api; 