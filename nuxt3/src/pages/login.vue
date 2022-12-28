<template>
  <NuxtLayout>
    <div class="container">
      <h1 class="heading">Please Login</h1>
      <form @submit.prevent="login">
        <div class="errors" v-if="errors">{{ errors }}</div>
        <div class="inputSet">
          <label for="username" class="green">Username:</label>
          <input type="text" name="username" id="username" class="green" required>
        </div>

        <div class="inputSet">
          <label for="password" class="green">Password:</label>
          <input type="password" name="password" id="password" class="green" required>
        </div>

        <div class="inputSet buttonContainer">
        <button type="submit">Login</button>
      </div>
      </form>
    </div>
  </NuxtLayout>
</template>

<script>
export default {
  setup() {
    const appConfig = useAppConfig();
    return { appConfig }
  },
  data() {
    return {
      isLoading: false,
      errors: null,
    }
  },
  methods: {
    login(e) {
      this.isLoading = true;

      const body = {
        "username": e.target.elements.username.value,
        "password": e.target.elements.password.value,
      }
      
      fetch("http://localhost:8000/" + "/get-api-token", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
      })
        .then(res => {
          if (!res.ok) {
            return res.json().then(json => {
              this.errors = json["non_field_errors"].join(", ");
              this.isLoading = false;
            })
          } else {
            return res.json().then(json => {
              this.isLoading = false;
              localStorage.setItem('API_token', json.token);
              this.$router.push("/")
            })
          }
        })

    }
  }
}
</script>

<style scoped>
@import "@/assets/forms.css";

.heading {
  text-align: center;
}
</style>
