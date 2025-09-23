<template>
  <div class="container">
    <div class="sidebar">作息时间表</div>

    <div class="title-bar">
      <div>冬春季时间<br><small>10月1日后开始实行</small></div>
      <div class="center">节次</div>
      <div>夏秋季时间<br><small>5月1日后开始实行</small></div>
    </div>

    <div class="divider"></div>

    <div class="time-table">
      <div class="time-row">
        <span class="left">8:00-8:50</span>
        <span class="center">第一节课</span>
        <span class="left">8:00-8:50</span>
      </div>
      <div class="time-row">
        <span class="left">9:00-9:50</span>
        <span class="center">第二节课</span>
        <span class="left">9:00-9:50</span>
      </div>
      <div class="time-row">
        <span class="left">10:10-11:00</span>
        <span class="center">第三节课</span>
        <span class="left">10:10-11:00</span>
      </div>
      <div class="time-row">
        <span class="left">11:10-12:00</span>
        <span class="center">第四节课</span>
        <span class="left">11:10-12:00</span>
      </div>
      <div class="time-row">
        <span class="left">14:00-14:50</span>
        <span class="center">第五节课</span>
        <span class="right">14:30-15:20</span>
      </div>
      <div class="time-row">
        <span class="left">15:00-15:50</span>
        <span class="center">第六节课</span>
        <span class="right">15:30-16:20</span>
      </div>
      <div class="time-row">
        <span class="left">16:10-17:00</span>
        <span class="center">第七节课</span>
        <span class="right">16:40-17:30</span>
      </div>
      <div class="time-row">
        <span class="left">17:10-18:00</span>
        <span class="center">第八节课</span>
        <span class="right">17:40-18:30</span>
      </div>
      <div class="time-row">
        <span class="left">19:10-20:00</span>
        <span class="center">第九节课</span>
        <span class="right">19:40-20:30</span>
      </div>
      <div class="time-row">
        <span class="left">20:10-21:00</span>
        <span class="center">第十节课</span>
        <span class="right">20:40-21:30</span>
      </div>
    </div>

    <div class="divider"></div>

    <div class="office-time">
      <div class="office-label">办公时间</div>
      <div class="office-row">
        <span class="left">08:00-12:00</span>
        <span class="center">上午</span>
        <span class="right">08:00-12:00</span>
      </div>
      <div class="office-row">
        <span class="left">14:00-18:00</span>
        <span class="center">下午</span>
        <span class="right">14:30-18:30</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
    body {
      font-family: "Microsoft YaHei", sans-serif;
      background-color: #f5f5f5;
      margin: 20px;
      color: #333;
    }

    .container {
      width: 95%;
      max-width: 800px;
      margin: auto;
      background-color: white;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
      overflow: hidden;
    }

    .title-bar {
      display: flex;
      justify-content: space-between;
      background-color: #3a7e8c;
      color: white;
      padding: 15px;
      border-radius: 10px 10px 0 0;
      font-size: 1.2em;
      font-weight: bold;
    }

    .title-bar div {
      text-align: center;
      padding: 5px;
    }

    .title-bar .center {
      flex-grow: 1;
    }

    .time-table {
      margin: 20px;
    }

    .time-row {
      display: flex;
      justify-content: space-between;
      background-color: #a6d0c7;
      border-radius: 10px;
      padding: 12px;
      margin-bottom: 8px;
      font-size: 1.1em;
      align-items: center;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .time-row span {
      flex: 1;
      text-align: center;
    }

    .time-row .left, .time-row .right {
      color: #1a3b66;
      font-weight: bold;
    }

    .time-row .right {
      color: #d32f2f;
    }

    .divider {
      height: 2px;
      background-color: #3a7e8c;
      margin: 15px 0;
      border: none;
      border-top: dashed 2px #3a7e8c;
    }

    .sidebar {
      position: absolute;
      left: 0;
      top: 0;
      width: 50px;
      height: 100%;
      background-color: #8ea0c0;
      color: white;
      padding: 20px 0;
      text-align: center;
      font-weight: bold;
      font-size: 1.2em;
      line-height: 1.8;
      transform: rotate(-90deg);
      transform-origin: left top;
    }

    .office-time {
      margin-top: 20px;
      background-color: #fff;
      padding: 10px;
    }

    .office-row {
      display: flex;
      justify-content: space-between;
      background-color: #ffeb3b;
      border-radius: 10px;
      padding: 12px;
      margin-bottom: 8px;
      font-size: 1.1em;
      align-items: center;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .office-row span {
      flex: 1;
      text-align: center;
    }

    .office-row .center {
      color: #333;
      font-weight: bold;
    }

    .office-label {
      background-color: #8ea0c0;
      color: white;
      padding: 10px;
      text-align: center;
      font-weight: bold;
      position: relative;
      top: -10px;
    
      border-radius: 5px;
    }
</style>