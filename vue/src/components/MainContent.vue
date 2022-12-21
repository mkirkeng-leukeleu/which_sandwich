<script>
import OrderView from './OrderView.vue';
import SandWichForm from './SandWichForm.vue';

export default {
    data() {
        return {
          isLoading: false,
          order: null
        };
    },
    created() {
      this.fetchOrder();
    },
    components: { SandWichForm, OrderView },
    methods: {
      fetchOrder() {
        this.isLoading = true;
        
        // ask API if there's an order already saved
        fetch(import.meta.env.VITE_API_URL + "/order")
          .then(res => res.json())
          .then(json => {
            this.order = (Object.keys(json).length == 0) ? null : json;
            this.isLoading = false;
          }) // no error handling :(
      },
      submitOrder(data) {
        this.isLoading = true;
        
        // submit an order to the API
        fetch(
          import.meta.env.VITE_API_URL + "/order",
          {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data) 
          }
        )
          .then(res => res.json())
          .then(json => {
            this.order = json;
            this.isLoading = false;
          }) // no error handling :(
      }
    }
}
</script>

<template>
  <div class="loading" v-if="isLoading">
    Loading...
  </div>
  <OrderView :orderData="order" v-else-if="order"/>
  <SandWichForm v-else @submitForm="submitOrder"/>

</template>
