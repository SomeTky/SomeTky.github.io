<template>
  <div class="container">
    <h1>西安交通大学-电子与信息学部软件学院-NotTky</h1>
    <div class="button-container">
      <button class="btn btn-primary" @click="showLessons">课表</button>
      <button class="btn btn-secondary" @click="showTimeTable">时间表</button>
      <button class="btn btn-primary" @click="toOtherWebsite('http://yjskq.xjtu.edu.cn')">考勤系统</button>

    </div>
  </div>
</template>

<script setup>

import { useRouter } from 'vue-router';

const router = useRouter()

function showLessons() {
  router.push("/lessons")
}

function showTimeTable() {
    router.push("/timetable")
}

function toOtherWebsite(url) {
  location.assign(url);
}

</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f8f9fa;
  padding: 20px;
  box-sizing: border-box;
  text-align: center;
}

h1 {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 1.8rem;
  font-weight: 500;
  color: #2c3e50;
  margin-bottom: 2rem;
  letter-spacing: 1px;
}

.button-container {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
}

.btn {
  padding: 12px 28px;
  border: none;
  border-radius: 50px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.btn:active {
  transform: translateY(0);
}

.btn-primary {
  background-color: #007bff;
  color: white;
}

.btn-primary:hover {
  background-color: #0056b3;
}

.btn-secondary {
  background-color: #28a745;
  color: white;
}

.btn-secondary:hover {
  background-color: #1e7e34;
}

/* 可选：添加更多颜色按钮 */
.btn-tertiary {
  background-color: #ffc107;
  color: #212529;
}

.btn-tertiary:hover {
  background-color: #e0a800;
}

/* 响应式适配 */
@media (max-width: 768px) {
  h1 {
    font-size: 1.4rem;
  }
  .btn {
    padding: 10px 20px;
    font-size: 0.95rem;
  }
}
</style>