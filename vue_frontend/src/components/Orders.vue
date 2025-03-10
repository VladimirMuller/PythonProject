<script setup>

import { CTable } from '@coreui/vue'


/*defineProps({
  msg: {
    type: String,
    required: true,
  },
})*/

    
const data = fetch("http://127.0.0.1:8000/api/orders", {
  mode: 'no-cors'
})
  .then(response => console.log(response))
  .catch(error => console.error(error));

  console.log(data);

/*
fetch(sign_in, {
      //mode: 'no-cors',
      credentials: 'include',
      method: 'POST',
      headers: headers
    })
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.log('Authorization failed : ' + error.message));
    */

    
    // const data = fetch("http://127.0.0.1:8000/api/orders", {mode: 'cors', headers: headers});
  
    // console.log(data);
  
  

  const columns = [
    {
      key: 'id',
      label: '#',
      _props: { scope: 'col' },
    },
    {
      key: 'Number',
      _props: { scope: 'col' },
    },
    {
      key: 'Customer',
      label: 'Heading',
      _props: { scope: 'col' },
    },
    {
      key: 'Date',
      label: 'Heading',
      _props: { scope: 'col' },
    },
  ]
  // todo feach data into items
  const items = [
    {
      id: 1,
      number: 'Mark',
      customer: 'Otto',
      date: '@mdo',
      _cellProps: { id: { scope: 'row' } },
    },
    {
      id: 2,
      class: 'Jacob',
      heading_1: 'Thornton',
      heading_2: '@fat',
      _cellProps: { id: { scope: 'row' } },
    },
  ]

</script>

<template>
    <div>
        <CTable :columns="columns" :items="items" />
    </div>
</template>