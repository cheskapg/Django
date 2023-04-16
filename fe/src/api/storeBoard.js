import { create } from "zustand";
import axios from "axios";

const useBoardStore = create((set) => ({
  boardModel: [],
  isLoading: false,

  getBoardList: () => {
    set({ isLoading: true });
    axios.get(`${process.env.API_URL}/details/`)
      .then((response) => {
        console.log(response.data);
        set({ boardModel: response.data, isLoading: false });
      })
      .catch((error) => {
        set({ isLoading: false });
      });
  },
}));
export default useBoardStore;