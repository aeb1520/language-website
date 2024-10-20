const API_BASE_URL = 'http://172.27.86.104:8080/api';

export const fetchData = async () => {
  const response = await fetch(`${API_BASE_URL}/endpoint`);
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
};

export default fetchData;