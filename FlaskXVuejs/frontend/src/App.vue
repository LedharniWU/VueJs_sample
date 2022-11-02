<template>
  <DragDropVue/>
</template>

<script>
import DragDropVue from './components/DragDrop.vue';


export default {
  name: 'App',
  components: {
    DragDropVue
  }
}
</script>

<style>
html,
  body {
      height: 100%;
  }

  body {
      display: flex;
      justify-content: center;
      align-items: center;
}
</style>
