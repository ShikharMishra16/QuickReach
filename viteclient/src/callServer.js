import axios from "axios";

const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://localhost:5000";

export const fetchShortData = async (a, b) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/shortd/${a}/${b}`);
    return response.data;
  } catch (error) {
    console.error("API Error:", error);
    throw error;
  }
};
