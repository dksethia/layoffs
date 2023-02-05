<script setup lang="ts">
import { ref } from "vue";
const props = defineProps(["p"]);
const p = ref(0);
setInterval(() => {
  if (p.value < props.p) {
    p.value += 2;
  }
}, 5);
</script>

<template>
  <div class="pie" :style="'--p: ' + p + '; --b: 15px; --c: #d5b4ff'">
    {{ Math.round(p) }}%
  </div>
</template>

<style scoped>
.pie {
  --w: 150px;
  width: var(--w);
  height: var(--w);
  aspect-ratio: 1;
  position: relative;
  display: inline-grid;
  place-content: center;
  margin: 5px;
  font-size: 25px;
  font-weight: bold;
  font-family: sans-serif;
}
.pie:before {
  content: "";
  position: absolute;
  border-radius: 50%;
  inset: 0;
  background: conic-gradient(var(--c) calc(var(--p) * 1%), #0000 0);
  -webkit-mask: radial-gradient(
    farthest-side,
    #0000 calc(99% - var(--b)),
    #000 calc(100% - var(--b))
  );
  mask: radial-gradient(
    farthest-side,
    #0000 calc(99% - var(--b)),
    #000 calc(100% - var(--b))
  );
}
</style>
