import axios from 'axios'

const service = axios.create({
  baseURL: 'http://127.0.0.1:5000', // 注意这里写你后端的地址
  timeout: 10000
})

service.interceptors.response.use(
  response => {
    const res = response.data
    if (res.status === 'fail') {
      return Promise.reject(new Error(res.message || 'Error'))
    }
    return res
  },
  error => {
    console.error('请求出错:', error)
    return Promise.reject(error)
  }
)

export default service