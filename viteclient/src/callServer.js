import axios from "axios";

export const fetchShortData = async (a, b) => {
  try {
    const response = await axios.get(`http://localhost:5000/shortd/${a}/${b}`);
    return response.data;
  } catch (error) {
    console.error("API Error:", error);
    throw error;
  }
};
