<template>
  <NuxtLayout>
    <h1 class="heading">Logging out...</h1>
  </NuxtLayout>
</template>

<script>
export default {
  setup() {
    definePageMeta({
      middleware: "require-auth"
    })

    const appConfig = useAppConfig();
    return { appConfig }
  },
  mounted() {
    this.logout();
  },
  methods: {
    logout () {
      // TODO: also delete token from backend
      localStorage.removeItem("API_token");
      localStorage.removeItem("username");

      this.$router.push("/");
    }
  }
}
</script>

<style scoped>
.heading {
  text-align: center;
}
</style>
