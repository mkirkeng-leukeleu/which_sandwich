<script>
import sandwiches from '../sandwiches';

export default {
    props: {
      orderData: {
        type: Object
      }
    },
    computed: {
      getSandwichName() {
        return sandwiches.filter((sandwich) => {
          return sandwich.id == this.orderData.sandwich
        })[0].name
      }
    }
}
</script>

<template>
  <div class="container">
    <div><h1>Last order</h1></div>
    <div>
      <p>
        <span class="green">Email: </span>{{ orderData.email }}
      </p>
      <p>
        <span class="green">Sandwich: </span>{{ getSandwichName }}
      </p>
      <p>
        <span class="green">Bread type: </span>{{ orderData.breadType }}
      </p>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: block;
}
</style>
