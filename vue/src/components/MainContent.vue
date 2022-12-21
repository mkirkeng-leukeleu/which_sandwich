<script>
import OrderView from './OrderView.vue';
import SandWichForm from './SandWichForm.vue';

export default {
    data() {
        return {
          isLoading: false,
          orderSent: false,
          order: {}
        };
    },
    components: { SandWichForm, OrderView },
    methods: {
      submit(data) {
        this.isLoading = true;
        
        // go to api
        setTimeout(() => {
          this.order = data;
          this.orderSent = true;
          this.isLoading = false;
        }, 3000)

      }
    }
}
</script>

<template>
  <div class="loading" v-if="isLoading">
    Loading...
  </div>
  <OrderView :orderData="order" v-else-if="orderSent"/>
  <SandWichForm v-else @submitForm="submit"/>

</template>
