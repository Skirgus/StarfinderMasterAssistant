<template>
  <div id="app">
    <div class="loginContainer">
      <div class="loginWrapper">
        <div class="loginTitle">
          Введите логин и пароль
        </div>
        <input type="text" class="inputData">
        <input type="text" class="inputData">
        <div class="sendAuthData">Отправить</div>
      </div>
    </div>
  </div>
</template>


<style>
#app {
  height: 100%;
  width: 100%;
}
.loginContainer {
  display: flex;
  justify-content: flex-end;
  background: #000;
}
.loginWrapper {
  display: flex;
  margin-right: 250px;
  width: 200px;
  height: 100px;
  flex-direction: column;
  margin-top: 20%;
  color: white;
  box-shadow: 0 0 60px white;
  border-radius: 5px;
}
.loginTitle{
  text-align: center;
  padding-top: 10px;
}
.inputData {
  margin-top: 15px;
  border-radius: 5px;
  padding: 0 8px;
}
.sendAuthData {
  width: inherit;
  height: 30px;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  font-size: 13px;
  text-align: center;
}
</style>
