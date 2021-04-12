// appfront/src/api/api.js
import axiosInstance from './index.js'

const axios = axiosInstance

export const getBooks = () => {return axios.get(`http://localhost:8000/api/books/`)}

export const postBook = (bookName, bookAuthor) => {return axios.post(`http://localhost:8000/api/books/`, {'name': bookName, 'author': bookAuthor})}