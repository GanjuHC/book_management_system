<template>
  <!-- 1. 把宽度改大一点，比如 80% 或 90% -->
  <div style="margin: 0 auto; width: 85%; padding-top: 50px;">
    <h1 style="text-align: center">图书管理系统</h1>

    <el-button type="primary" @click="openAddDialog" size="small" style="margin-bottom: 20px;">
      添加图书
    </el-button>

    <!-- 2. 给表格加上 stripe 斑马纹，更好看 -->
    <el-table :data="books" style="width: 100%" border stripe>
      
      <!-- 3. 给部分列加上 min-width，防止被挤得太窄 -->
      <el-table-column label="编号" prop="book_number" width="100" />
      <el-table-column label="书名" prop="book_name" min-width="150" />
      <el-table-column label="类型" prop="book_type" width="100" />
      <el-table-column label="价格" prop="book_prize" width="100" />
      <el-table-column label="作者" prop="author" width="120" />
      
      <!-- 4. 给出版社加上 show-overflow-tooltip，太长会变成省略号，鼠标放上去显示全称 -->
      <el-table-column label="出版社" prop="book_publisher" min-width="150" show-overflow-tooltip />
      
      <!-- 5. 重点：给操作列加上 fixed="right"，让它固定在右侧，并给个固定宽度 -->
      <el-table-column align="center" label="操作" width="160" fixed="right">
        <template #default="scope">
          <el-button size="small" @click="openEditDialog(scope.row)">编辑</el-button>
          <el-button size="small" type="danger" @click="handleDelete(scope.row.id)">删除</el-button>
        </template>
      </el-table-column>
      
    </el-table>

    <!-- 添加 / 编辑共用弹窗 -->
    <el-dialog :title="isEdit ? '编辑图书' : '添加图书'" v-model="dialogVisible" width="30%">
      <el-form :model="bookForm" label-width="100px">
        <el-form-item label="编号">
          <el-input v-model="bookForm.book_number" />
        </el-form-item>
        <el-form-item label="书名">
          <el-input v-model="bookForm.book_name" placeholder="请输入书名" />
        </el-form-item>
        <el-form-item label="类型">
          <el-input v-model="bookForm.book_type" />
        </el-form-item>
        <el-form-item label="价格">
          <el-input v-model.number="bookForm.book_prize" />
        </el-form-item>
        <el-form-item label="作者">
          <el-input v-model="bookForm.author" />
        </el-form-item>
        <el-form-item label="出版社">
          <el-input v-model="bookForm.book_publisher" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm">提交</el-button>
          <el-button @click="dialogVisible = false">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script setup>
import { reactive, ref, onMounted } from 'vue'
import request from './utils/request'
import { ElMessage, ElMessageBox } from 'element-plus'

const books = reactive([])
const dialogVisible = ref(false)
const isEdit = ref(false)

const bookForm = reactive({
  id: null,
  book_number: '',
  book_name: '',
  book_type: '',
  book_prize: '',
  author: '',
  book_publisher: ''
})

// 获取列表数据
const fetchBooks = () => {
  request.get('/books').then(res => {
    books.splice(0, books.length, ...res.results)
  })
}

// 打开添加弹窗
const openAddDialog = () => {
  isEdit.value = false
  Object.assign(bookForm, {
    id: null, book_number: '', book_name: '', book_type: '',
    book_prize: '', author: '', book_publisher: ''
  })
  dialogVisible.value = true
}

// 打开编辑弹窗
const openEditDialog = (row) => {
  isEdit.value = true
  Object.assign(bookForm, row)
  dialogVisible.value = true
}

// 提交表单（区分新增和修改）
const submitForm = () => {
  // 加一层简单校验
  if (!bookForm.book_name || !bookForm.book_number) {
    ElMessage.warning('书名和编号不能为空')
    return
  }
  
  const req = isEdit.value
    ? request.put(`/books/${bookForm.id}`, bookForm)
    : request.post('/books', bookForm)

  req.then(() => {
    dialogVisible.value = false
    fetchBooks()
    ElMessage.success(isEdit.value ? '修改成功' : '添加成功')
  }).catch(err => {
    // 捕获后端的报错
    ElMessage.error('操作失败：' + (err.message || '服务器异常'))
  })
}

// 删除功能
const handleDelete = (id) => {
  ElMessageBox.confirm('确认删除？', '提示', { type: 'warning' })
    .then(() => {
      request.delete(`/books/${id}`).then(() => {
        fetchBooks()
        ElMessage.success('删除成功')
      })
    })
    .catch(() => {})
}

// 页面加载时获取数据
onMounted(() => {
  fetchBooks()
})
</script>