<template>
  <NuxtLayout>
    <div class="wrapper">
      <div class="orderlist">
        <div v-for="order in data">
          <OrderView :orderData="order"/>
        </div>
      </div>
      <NuxtLink to="/">
        Go back to the homepage...
      </NuxtLink>
    </div>
  </NuxtLayout>
</template>

<script>
export default {
  setup() {
    definePageMeta({
      middleware: "require-auth",
    }) // options API doesn't seem to work

    const appConfig = useAppConfig();
    return { appConfig };
  },
  data() {
    return {
      data: null
    }
  },
  mounted() {
    fetch(this.appConfig.API_URL + "/orders", {
      headers: {
          "Content-Type": "application/json",
          "Authorization": "Token " + localStorage.getItem("API_token")
        }
    })
      .then(res => res.json())
      .then(json => {
        this.data = json;
      }) // no error handling :(
  }
}
</script>

<style scoped>
.orderlist {
  display: flex;
  flex-direction: column;
  overflow-y: scroll;
  max-height: 75vh;
}

</style>
