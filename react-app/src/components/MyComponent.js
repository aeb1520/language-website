
import React, { useEffect, useState } from 'react';
import { fetchData } from './apiService';

const MyComponent = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const getData = async () => {
      try {
        const result = await fetchData();
        setData(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    getData();
  }, []);

  return <div>{data ? JSON.stringify(data) : 'Loading...'}</div>;
};

export default MyComponent;
