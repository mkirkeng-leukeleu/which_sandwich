<template>
  <!-- <pre v-if="data">{{ data }}</pre> -->
  <header>
    <MainHeader/>
  </header>
  
  <main>
    <div v-for="order in data" class="container">
      <OrderView :orderData="order"/>
      <br />
    </div>
  </main>
</template>

<script>
export default {
  setup() {
    const appConfig = useAppConfig();
    return { appConfig };
  },
  data() {
    return {
      data: null
    }
  },
  mounted() {
    fetch(this.appConfig.API_URL + "/orders")
      .then(res => res.json())
      .then(json => {
        this.data = json;
      }) // no error handling :(
  }
}
</script>

<style scoped>
header {
  line-height: 1.5;
}

main {
  padding: 1rem;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

@media (min-width: 1024px) {
  main::before {
    position: absolute;
    left: 0;
    content: " ";
    border-left: 1px solid var(--color-border);
    height: 80%;
  }

  header {
    display: flex;
    place-items: center;
  }
}
</style>
