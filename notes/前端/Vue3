# 项目构建

```bash
npm create vue@latest
```





# Vue组件的基本结构

```vue
<template>
    
</template>

<script setup lang="ts">
    
</script>

<style scoped>

</style>
```

# 其他知识

​	这一章放一些杂七杂八的知识点，由于学习过程中难免会有知识穿插，为了统一管理，均在放此处。

## 配置npm run在0.0.0.0

#### 1. Vite (最常见)

如果你在使用 Vite，可以通过修改 `vite.config.js` 或 `vite.config.ts` 文件来实现。

```javascrip
// vite.config.js
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0', // 设置为 0.0.0.0 即可
    port: 5173, // 可选，设置端口
  },
});
```



## nanoid

​	可以随机生成一个唯一id。

```cmd
npm i nanoid
```

```vue
<script setup lang="ts">
	import {nanoid} from "nanoid"
    let id = nanoid()
</script>
```





## defineExpose

​	这个函数通常放在组件的最后面，用来定义对外暴露的属性。

例如：

​	在Person组件中：
```vue
<script setup lang="ts">
    import { ref } from 'vue'
    let testText = '会有人发现我吗？'
</script>
```

​	在APP组件中访问Person实例，看看会得到什么：

```vue
<template>
  <Person ref="ren"/>
</template>

<script lang="ts" setup name="App">
  import Person from './components/Person.vue'
  import { ref } from 'vue'
  let ren = ref()
  console.log(ren)
</script>
```

​	得到的结果是：

![image-20250426153645858](D:\notes\vue3-pic\image-20250426153645858.png)

​	下面我们将testText暴露一下：

```vue
<script setup lang="ts">
    import { defineExpose } from 'vue'
    let testText = '会有人发现我吗？'
    defineExpose({testText})
</script>
```

​	得到的结果是：

![image-20250426154040476](D:\notes\vue3-pic\image-20250426154040476.png)

## axios

1. 网络请求库
2. 同一套代码运行在node.js或浏览器中
3. 发起一个get请求
4. 发起一个post请求



​	axios是一个网络请求库，一套代码可以运行在浏览器或node.js上。可以安装vue-axios以在vue中使用。

```cmd
npm install vue-axios
```

​	发起一个get请求示例：

```ts
let picture = ref('')
function getPicture() {
    axios.get("https://dog.ceo/api/breed/pembroke/images/random")
        .then((response)=>{
            picture.value = response.data.message
        }).catch(()=>{
            alert('获取图片异常')
        })
}
```

​	get请求传递参数可以直接写在url里面，也可以对象的形式写在get方法中的第二个参数上。

​	下面是await/wait写法

```ts
async function getPicture() {
    try{
        const response = await axios.get("https://dog.ceo/api/breed/pembroke/images/random")
        picture.value = response.data.message
    }
    catch (error){
        alert('图片获取失败')
    }
}
```

​	==这里点到为止后续需要对axios进行更详细的学习==







# setup

​	组合式api可以用<script setup>来避免每次书写setup函数。

​	在<script setup>标签中，无需将定义的数据返回就可以在<template>标签中访问到。

# ref\reactive

​	可以定义响应式基本数据也可以定义响应式对象，但是相比reactive，其定义的响应式对象是浅层的。

​	reactive只可以定义响应式对象，其定义的响应式对象是深层的。

​	reactive有一个弊端就是无法直降将整个对象换成另外一个，即使重新生成一个reactive对象也无法将页面变换。原因是新生成的对象已经不是在页面显示上的那个了，自然不会响应。如果实在需要修改的话可以使用：

```js
Object.assign('oldObject', 'newObject')
```

​	==ref定义的变量在字符串模板里面可以不用.value就可以使用==

## Using ref to get the dom

If you use vue, you may not use document to get the element in html. In another way, you should declare a const variable of ref, and then write the ref variable in the html attribute. Like this:

```vue
<template>
	<div ref='tkytest'>
        
    </div>
</template>

<script>
	import {ref} from "vue"
    const tkytest = ref()
</script>
```

tkytest.value is the dom of the div element.



# toRef\toRefs

​	对于响应式的数据，直接结构会失去响应式。可以使用本节两个函数保持响应式。	

​	解构一个对象中的各个元素，toRef一次只能解构一个，toRefs可以一次性都解构。

​	e.g <template>如下

```vue
<template>
    <h1>name:{{ name }}</h1>
    <h1>age: {{ age }}</h1>
</template>
```

​	对于toRef，使用方式如下：

```vue
<script setup lang="ts">
    import { reactive, toRef} from 'vue';
    let Person = reactive({name: 'san zhang', age: 25})
    let name = toRef(Person, 'name')
    let age = toRef(Person, 'age')
</script>
```

​	对于toRefs，使用方式如下：

```vue
<script setup lang="ts">
    import { reactive, toRefs} from 'vue';
    let Person = reactive({name: 'san zhang', age: 25})
    let {name, age} = toRefs(Person)
</script>
```

# v-model

​	结合输入框，可以让响应式变量与输入框中的内容保持一致。

​	v-model.number可以设定绑定值的类型。

# computed计算属性

​	方法没有缓存，计算属性有缓存。

​	compute传入一个函数

​	compute的返回值是一个"computeRef"，因此访问时需要使用.value

​	compute有两种书写方式，一种只可读，另一种可读可写。

​	template如下：

```vue
<template>
    <input v-model="firstname"> <br>
    <input v-model="lastname"> <br>
    <span>全名计算器: {{ fullname }}</span>
</template>
```

​	只读写法是直接在compute中返回值：

```vue
<script setup lang="ts">
    import { ref, computed} from 'vue';
    
    let firstname = ref('zhang')
    let lastname = ref('san')
    let fullname = computed(() => {
        return firstname.value.slice(0, 1).toUpperCase() + firstname.value.slice(1) + ' ' + lastname.value
    })
</script>
```

​	对于可修改，这里有一个误区。当我们修改firstname的时候，fullname也被修改了，但这并不是直接对fullname修改，所谓可写，是指可以直接对fullname修改。

​	需要写成如下形式，其中get()函数中返回读取时的值, set(value)中写进行修改时的逻辑，其中value是修改值。

​	给界面加一个按钮，按下按钮时，修改fullname为“Tiankaiyuan”：

```vue
<template>
    <input v-model="firstname"> <br>
    <input v-model="lastname"> <br>
    <span>全名计算器: {{ fullname }}</span><br>
    <button @click="changeFullName">修改fullname</button>
</template>
```

​	可修改computed写法如下：

```vue
<script setup lang="ts">
    import { ref, computed} from 'vue';
    
    let firstname = ref('zhang')
    let lastname = ref('san')
    let fullname = computed({
        get() {
            return firstname.value.slice(0, 1).toUpperCase()
                + firstname.value.slice(1) + ' ' + lastname.value
        },
        set(value) {
            let [tempfirst, templast] = value.split(' ')
            firstname.value = tempfirst
            lastname.value = templast
        }
    })

    function changeFullName() {
        fullname.value = "Tian kaiyuan"
    }
</script>
```

# watch

watch的第一个参数是监视的对象，第二个参数是回调函数，第三个参数是配置==对象==

watch 只能监视4种（传入参数），返回值是，

​	watch用来监视响应式数据的变化，第一个参数只能传入四种值

  1. ref

  2. reactive

  3. 函数返回一个值

  4. 一个包含上述内容的数组

     watch的返回值可以作为函数调用，调用后将不再继续监视。

## watch-情况一

eg：

​	当修改后的值大于修改前值的二倍时，alert。

```vue
<template>
    <span>{{ sum }}</span> <br>
    <input v-model="input">
    <button @click="changeSum">修改</button>
</template>

<script setup lang="ts">
    import { ref, watch} from 'vue';
    let sum = ref(1)
    let input
    
    const stopwatch = watch(sum, (newValue, oldValue) => {
        if (newValue > 2 * oldValue) {
            alert("this is a alert")
        }
    })

    function changeSum() {
        if (input) {
            sum.value = parseInt(input)
        }
    }
</script>
```

​	如过相同的方式监视一个对象，那么它监视的是整个对象的地址值，意味着如果修改对象中的某一个属性，并不能触发watch，只有将整个对象改掉，才会触发watch。

## watch-情况二

​	监视一个对象中的某个属性变化，需要在watch的配时参数对象中，另deep为true。

```vue
<script setup>
    const stopwatch = watch(Person,
        (newValue, oldValue) => {console.log(Person, newValue, oldValue)},
        {deep: true})
</script>
```

​	此时需要注意newValue和oldValue中的值相等且均为newValue的值。

*tips：配置对象的immediate属性如果设置为true，watch将会在程序运行初被调用一次*

## watch-情况三

​	监视一个reactive对象时，无论是对象整体变动，还是其中的某个属性变动，都会被监视到。==即默认深度监视，且无法关闭==。

​	需要注意的是整体变动并不是把整个对象换了（reactive是不可以这么操作的），指示用Object.assign将值重新分配了。

## watch-情况四

​	如果只想监视响应式对象中的某个基本属性，不可以直接传入对象.属性的方式，需要传入一个函数，该函数返回想要监视的属性。（这个函数就叫getter函数）。

​	如果只想监视响应式对象中的某个对象属性，能直接监听也可以写成函数，==建议写成函数==。

​	如果传入对象，不能监听整个对象被改变的情况，写成函数则可以避免这个问题。

## watch-情况五

​	如果想监视多个数据上述数据，可以把这些数据写到一个数组里面。

## watchEffect

​	watchEffect所能实现的功能与watch一致，不过watchEffect不需要指定要监视谁，它会根据逻辑自动分析需要监视的变量。

eg：

```vue
<template>
    <h1>水温：{{ temp }}</h1><br>
    <h1>水位：{{ height }}</h1><br>
    <button @click="changeHeight">增加温度</button><br>
    <button @click="changeTemp">增加水位</button>
</template>
```

```vue
<script setup lang="ts">
    import {watchEffect, ref} from 'vue'
    let temp = ref(0)
    let height = ref(0)

    function changeTemp() {
        temp.value += 1
    }
    function changeHeight() {
        height.value += 1
    }

    watchEffect(()=>{
        if (temp.value > 10 && height.value > 10) {
            alert('可以了可以了')
        }
    })
</script>
```



# vue编译为一页所产生问题的解决方案

## 1. 局部样式

​	通常只使用一个<style>标签来书写样式表，此样式表效果会影响到全局

​	改写成局部样式即可<style scoped>

## 2. 使用ref而不是id

​	如果一个标签的id为title，此时另一个组件中也有id为title的标签，那么编译后获取id为title的标签内容时，会得到在单页面最先出现的id为title的标签的值。

​	可以使用ref来解决这个问题：

# defineProps

​	defineProps可以在父组件中给子组件传递参数，defineProps接受一个数组参数，返回值是一个对象。

​	在App组件中向Person传递msg：

```vue
App.vue
<template>
  <Person msg="This is a message"/>
</template>
```

​	在Person组件中接收：

```vue
Person.vue
<script setup lang="ts">
    import { defineProps } from 'vue'
    defineProps(['msg'])
</script>
```

​	这种传递方式，msg被直接暴露在<template>标签中，可以通过双花括号使用：

```vue
Person.vue
<template>
    <div>
        <ul>
            <li>{{ msg }}</li>
        </ul>
    </div>
</template>
```

​	==上述方式传递的是一个字面量，下面传递一个script对象==

​	传递时使用v-bind即可

```vue
App.vue
<template>
  <Person :msg="personlist"/>
</template>
```

```vue
Person.vue
<template>
    <div>
        <ul>
            <li v-for="item in msg">{{ item.name}}-{{ item.age }}</li>
        </ul>
    </div>
</template>
```

​	这种写法不会对传入的参数进行检查，可以使用泛型或类型指示或defineProps的参数指定来实现。

```vue
<script setup lang="ts">
    import { defineProps } from 'vue'
    import {type persons} from '@/types/index'
    defineProps<{list: persons}>()
</script>
```

​	==下面是限制所传参数的必要性==

​	默认情况下是必须要传递的，以紧挨着的上面的代码为例，直接在list的后面添加上‘？’即可实现可传可不传：

```vue
<script setup lang="ts">
    import { defineProps } from 'vue'
    import {type persons} from '@/types/index'
    defineProps<{list?: persons}>()
</script>
```

​	当然，在用户可以不传递参数的情况下，可以设置一个默认值。在vue3中，施加默认值需要使用withDefaults函数。

​	==withDefaults的第二个参数，即默认值对象中，属性的值应写成函数的形式==。

```vue
<script setup lang="ts">
    import { defineProps } from 'vue'
    import {type persons} from '@/types/index'
    withDefaults(defineProps<{list?: persons}>(), {
        list: ()=>[{name: 'tiankaiyuan', age:23}]})
</script>
```

# 生命周期

​	生命周期幼教生命周期函数、生命周期勾子。

| 生命周期 | 执行函数                     |
| -------- | ---------------------------- |
| 创建阶段 | setup                        |
| 挂载阶段 | onBeforeMount, onMounted     |
| 更新阶段 | onBeforeUpdate, onUpdated    |
| 卸载阶段 | onBeforeUnmount, onUnmounted |

​	Vue3的创建过程是“深度优先搜索”的，因此子组件的挂载早于父组件的挂载。

# 自定义hooks

​	为了实现vue3中组件式的数据方法“聚合”，可以将一个“对象”写到一个ts文件中，命名为useXXX（名称不强制）。

​	使用如下方式将其暴露：

```ts
//usePerson.ts
import {ref} from "vue"

export default function() {
    let sum = ref(0)
    function add() {
        sum.value += 1
    }

    return {sum, add}
}
```

​	在需要用到这个对象的地方import该文件，使用函数调用的方式获取数据和方法。

```vue
<script setup lang="ts">
    import usePerson from '@/hooks/usePerson'
    const {sum, add} = usePerson()
</script>

<template>
    <div>
        <h1>{{ sum }}</h1><br>
        <button @click="add">加一</button>
    </div>
</template>
```

# 路由

​	==一般组件放到components文件夹下，路由组件放在pages/views文件夹下==

## 基本页面切换	

​	本节实践一个例子，介绍vue的路由。

​	首先需要安装vue-router，通常在src文件夹下再创建一个router文件夹，在其中创建ts文件作为路由器。

```cmd
npm install vue-router
```

​	这里假设我们有三个页面，分别是MainHtml， Picture， About。这三个页面分别是vue组件，跟前面教程中的Person一样。

​	下面是创建路由器的模板：

​	其中createRouter（）中传入一个配置对象，routes是路由规则，注意其格式。createWebHistory是路由器的工作模式，后面会详解介绍。

```ts
import {createRouter, createWebHistory} from "vue-router"
import MainHtml from "@/components/MainHtml.vue"
import HelloWorld from "@/components/HelloWorld.vue"
import Picture from "@/components/Picture.vue"

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/', component:MainHtml},
        {path: '/picture', component: Picture},
        {path: '/about', component: HelloWorld}
    ],
})

export default router
```

​	==tips:这里的 export default router相比已经很熟悉了，是为了外部文件能够调用而暴露出去==

​	接下来，需要在main.ts中使用路由器，使用use方法。

```ts
import { createApp } from 'vue'
import App from './App.vue'
import router from "@/router/index"

const app = createApp(App)
app.use(router)
app.mount("#app")
```

​	==特别注意，mout需要放在所有use的后面==

​	对于vue路由，有两个组件要用，分别是<RouterLink>和<RouterView>。其中RouterLink代替<a>，<RouterView>用来展示路由的界面。如果没有RouterView会导致路由的页面没有地方显示。

​	<RouterLink>中有两个常用属性，to是路由路径，active-class是激活时的样式表（一般是高亮或其他指示效果）。

​	如下所示：

```vue
<template>
  <div>
    <h1>路由测试</h1>
    <!-- 导航栏 -->
    <div class="navigation">
      <RouterLink to="/" class="tky">首页</RouterLink>
      <RouterLink to="/picture" class="tky">狗狗图片</RouterLink>
      <RouterLink to="about" class="tky">关于</RouterLink>
    </div>
    <!-- 展示栏 -->
     <div>
        <RouterView />
     </div>
  </div>
</template>
```

## 路由器工作模式

​	history模式用createWebHistory()，URL中不带#，与传统一致，不过需要额外的后端配置。

​	hash模式用createWebHashHistory，URL中携带#，无需后端配置，不过在SEO优化方面较差。（俺也不知道SEO是啥）

## 命名路由

​	在<RouterLink>标签中的to属性除了直接填写路由字符串外，也可以写成对象形式。在路由器中的路由对象中可以添加一个name属性，为该路由命名，配合to属性的对象，可以直接实现名称路由。

```ts
const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/', component:MainHtml},
        {name: 'dogs', path: '/picture', component: Picture},
        {path: '/about', component: HelloWorld}
    ],
})
```

​	可以看第二条路由加了name属性，相应的，在页面中可以使用name来路由。

```ts
<div class="navigation">
  <RouterLink to="/" class="tky">首页</RouterLink>
  <RouterLink :to="{name: 'dogs'}" class="tky">狗狗图片</RouterLink>
  <RouterLink to="about" class="tky">关于</RouterLink>
</div>
```



## 路由嵌套

​	在一个路由对象中新增一个children属性，其值是一个路由对象数组，作为子路由对象，path属性是不需要加'/'的。

```ts
const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/', component:MainHtml
        },
        {name: 'dogs', path: '/picture', component: Picture},
        {
            path: '/about', component: HelloWorld,
            children:[
                {
                    path: 'tky',
                    component: tkyView
                }
            ]
        }
    ],
})
```

## 路由传参

​	可以使用URL字符拼接的方式直接传参，使用v-bind时，需要使用模板字符串+${}的形式嵌入表达式。

```vue
<RouterLink :to="`/about/tky?message=${msg}`">tky</RouterLink>
```

​	在接收参数时，从"vue-router"中导入useRoute，通过其query属性获得参数。

```vue
<script>
	 let query = toRef(useRoute().query)
</script>
```

​	上文说到<RouterLink>的to属性可以传入对象，在对象中的query属性填入要穿的参数也是可以实现上述功能的。

```vue
<template>
<RouterLink :to="{
        path: '/about/tky',
        query: {
            msg: 'what are you doing now?'
        }
    }">tky</RouterLink>
</template>
```

​	还可以使用params传参使用该方法时，to属性中使用url字符串拼接或者使用对象。在使用对象传参时，不可用path属性，只能用name。

​	使用该方法需要在路由器中为参数占位，如下path所示：

```ts
{name: 'dogs', path: '/picture/:id/:msg', component: Picture}
```

​	使用props参数可以简化params参数的传递。在路由器中设置props属性为true。

## 路由的props配置

​	在使用query传递参数时，可以使用props配置结合defineProps简化获取参数的流程。

​	首先在路由器中配置一个props函数，函数第一个参数是路由，该函数returnprops：
```ts
{
    path: 'tky',
    component: tkyView,
    props(route){
        return route.query
    }
}
```

​	在对应的界面直接使用defineProps获取参数即可。==不要忘了import==

```vue
<script setup lang="ts">
    import {defineProps} from "vue"
    defineProps(["msg"])
</script>
```

​	prop除了写成函数形式也可以写成对象形式，但是对象形式下没有传入参数，以为着只能写成“死”数据，并不实用。

​	对于组件的props，可以在标签上直接传入参数非常方便，但对于页面来说，代码中并没有其标签的书写，因此只能够在路由器中（index.ts）配置props。

## 路由的replace属性

​	默认情况下是push模式，可以在<RouterLink>标签中加入replace改成replace模式，即<RouterLink replace>。

​	如何从浏览器界面判断当前是push模式还是replace模式？可以注意网页左上角的返回按钮，如果点开新的页面可以返回到上一个页面，则当前为push模式，否则为replace模式。

​	==tips：push会留下“历史记录”，replace不会==

## 路由的编程式导航

$$
useRouter\\
.push方法\\
to属性可以写什么push就可以写什么\\
条件跳转\\
$$



​	上文提到的跳转方式是使用<RouterLink>标签，这种方法是没有办法在<script>中使用的。在程序中使用useRouter即可实现程序中跳转。

```vue
<script>
    import {useRouter} from 'vue-router'
</script>
```

​	可以使用push方法或者replace方法，其传入内容与to标签一致。

​	这里实践一个返回按钮：

```vue
<template>
	<button @click="backPage">返回</button>
</template>
<script setup lang="ts">
    import {useRouter} from 'vue-router'
    let router = useRouter()
    function backPage() {
        router.push({
            path: '/'
        })
    }
</script>
```

## 路由的重定向

​	将component属性替换为redirect属性即可实现重定向。

​	这里我们将'/'重定向到'/picture'：

```vue
<script setup lang="ts">
	const router = createRouter({
        history: createWebHistory(),
        routes: [{ path: '/',redirect: '/picture' }]})
</script>
```

# pinia

​	集中式状态管理组件。应当将需要共享的数据交由集中式状态管理组件管理。

​	对于需要共享的数据的理解，可以思考这样一个需求，通过登录验证系统获取了用户的头像，昵称，id信息等，当用户点进主页时需要展示其头像账号信息。该需求可以将此类数据放在pinia中，在别的界面通过pinia获取。

## 安装pinia

```cmd
npm i pinia
```

​	在main.js中使用pinia

```ts
import {createPinia} from "pinia"
const pinia = createPinia()
app.use(pinia)
```



## pinia的存取

​	规范化一些，在src文件夹下创建一个store文件夹用来存储pinia数据。

​	新建一个ts文件用来创建一个piniastore,这个文件夹中创建一个count.ts（这里教程视频里是小写，也许pinia就是用小写来命名吧）内容如下：

```ts
import {defineStore} from "pinia"
export const useCountStore = defineStore('count', {
    state() {
        return {
            sum: 0
        }
    }
})
```

​	defineStore的第一个参数是名称，第二个参数是一个配置对象，配置对象中的state()函数用来返回store中的值。

​	使用时，在组件中import这个useCountStore即可，该函数返回的是一个reactive对象。

```vue
<script>
	import {useCountStore} from "@/store/count"
    const countStore = useCountStore()
    console.log(countStore.sum)
</script>
```

## 修改pinia数据的其他方式

$$
action修改方式,里面放置的是一个一个动作方法\\
action方式相当于给pinia store对象实现一些方法，外部通过调用这些方法来实现逻辑操作\\
在action里可以this.方法获取值，也可以用\$state.获取值\\
面相对象的意义就在与让数据有逻辑（限制最大值，一个简单的例子）\\
$$

​	在useCountStore中我们多添加几个数据，然后一次性修改一下：

```ts
export const useCountStore = defineStore('count', {
    state() {
        return {
            sum: 0,
            name: "tiankaiyuan",
            job: "software engineer"
        }
    }
})
```

```vue
<script>
	countStore.$patch({
            sum: 666,
            name: 'nottky',
            job: 'reader'
        })
</script>
```

​	如果采用上一节一个一个修改的方式，系统一共会对pinia对象执行三次修改，这种方法一次到位。

​	还可以在pinia配置对象中添加一个actions属性，该属性实现操作该对象的一些方法。在actions中可以使用this获取数据，也可以方法$state方法获取数据对象。

```ts
export const useCountStore = defineStore('count', {
    actions:{
        add(value: number){
            this.sum += value
        }
    },
    state() {
        return {
            sum: 0,
            name: "tiankaiyuan",
            job: "software engineer"
        }
    }
})
```

同样可以用$state（多此一举）：

```ts
export const useCountStore = defineStore('count', {
    actions:{
        add(value: number){
            this.$state.sum += value
        }
    },
    state() {
        return {
            sum: 0,
            name: "tiankaiyuan",
            job: "software engineer"
        }
    }
})
```

​	使用的时候直接像调用对象的方法一样即可：

```vue
<script>
	function add() {
        countStore.add(n.value)
    }
</script>
```

## storeToRef

​	如果直接使用toRefs性能太差，不推荐，建议使用storeToRefs，该函数只关注store中的数据，不会对方法进行包裹。

​	该函数需要从pinia中import。

## getters

​	“如果你对目前的数据不满意，那么可以用getter来加工”（待深入理解），类似于一个计算属性。

​	假设有如下数据：

```ts
state() {
        return {
            sum: 0,
            name: "tiankaiyuan",
            job: "software engineer"
        }
}
```

​	希望有一个属性是name-job形式，就可以将该属性卸载getter里面。

```ts
export const useCountStore = defineStore('count', {
    state() {
        return {
            sum: 0,
            name: "tiankaiyuan",
            job: "software engineer"
        }
    },
    getters:{
        tkytest:state=>state.name + '-'  + state.job
    }
})
```

​	在组件中就可以直接访问tkytest属性。==记住需要传入state函数就可以了==

## $subcribe

​	pinia中的watch。

​	接受两个参数，第一个参数我们不关注他，主要是第二个参数，第二个参数是修改后的值。

## store组合式写法

​	简单来说就是数据函数直接定义好之后return出去。这里不需要再管什么actions和getter，直接定义相关方法就可以return回去，对于getter，直接用computed属性替换即可。

```ts
export const useCountStore = defineStore('count', ()=>{
    let sum = ref(0)
    let name = ref("tiankaiyuan")
    let job = ref("software engineer")
    let tkytest = computed(()=>{
        return name.value + '-' + job.value
    })

    function add(value: number) {
        sum.value += value
    }
    return {sum, name, job, tkytest, add}
})
```

​	推荐使用组合式方法。（vue3拥抱组合式和ts）。

# 组件通信

## props

​	父穿子：	

​	详见之前的笔记。

​	子传父：

​	父需要先给子传一个函数，子直接调用这个函数，数据来源于子，函数施加的影响在父身上。

​	父这边如下所示：

```vue
<template>
	<h1>{{ tky }}</h1>
	<Child :car="car" :tkytest="getTky"/>
</template>

<script setup lang='ts'>
	import Child from './Child.vue'
	import {ref} from 'vue'
	// 数据
	let tky = ref('')
	// 方法
	function getTky(value: string) {
		tky.value = value
	}
</script>
```

​	注意在父这里，函数的名称叫getTky，传给子的时候名字改为了tkytest：

```vue
<template>
	<button @click="tkytest(msg)">你是不是神经病</button>
</template>

<script setup lang="ts" name="Child">
	import {ref} from 'vue'
	// 数据
	let msg = ref('你咋知道')
	// 声明接收props
	defineProps(['tkytest'])
</script>
```

​	有点像儿子在教老子怎么说话哈哈哈哈。

## 自定义事件

​	在父这一端可以自定义一个时间，并且给该时间分配一个处理函数。把这个时间传递给子，子通过defineEmits来获取父传递过来的各个事件名称，并且可以用defineEmits返回的对象来触发事件（假设返回的对象名称为emit）。触发事件之间传递的参数可以直接写在emit的第二第三等等参数位置。

​	父的代码如下：

```vue
<template>
  <div class="father">
	<h1>{{ msg }}</h1>
    <Child @tky="tkyEvent"/>
  </div>
</template>

<script setup lang="ts" name="Father">
  import Child from './Child.vue'
	import { ref } from "vue";
	let msg = ref('')
	function tkyEvent(value:string) {
		msg.value = value
	}
</script>
```

​	子的代码如下：

```vue
<template>
  <div class="child">
	<button @click="tkyButton">你是我爸爸吗</button>
  </div>
</template>

<script setup lang="ts" name="Child">
	const emit = defineEmits(["tky"])
	function tkyButton() {
		emit("tky", '你咋知道')
	}
</script>
```

​	==文档中建议事件的命名方式为case命名法==

## mitt

$$
emitter.all\\
emitter.emit\\
emitter.off\\
emitter.on\\
任意组件通信\\
$$



​	mitt是一个插件，可以实现任意组件之间的通信（很小的一个插件）。

```cmd
npm install mitt
```

​	按照推荐的格式，在项目文件夹下创建一个utils文件夹，在里面创建emitter.ts。该文件中引入这个插件：

```ts
// 引入mitt
import mitt from 'mitt'

// 调用mitt得到emitter，emitter能：绑定事件、触发事件
const emitter = mitt()

// 暴露emitter
export default emitter
```

​	emitter一共有四个方法，all, emit, on, off，其中all是获取所有定义的事件，emit触发事件，on绑定新事件，off解绑事件。	

​	下面我们来实现一个两个子对话的页面：

​	child1代码如下：

```vue
<template>
  <div class="child1">
    <h1>{{ text }}</h1>
	<input v-model="msg">
	<button @click="emitter.emit('child2Get', msg)">Send</button>
  </div>
</template>

<script setup lang="ts" name="Child1">
	import {ref, onUnmounted} from 'vue'
	import emitter from '@/utils/emitter';
	let text = ref('')
	let msg = ref('')
	
	emitter.on("child1Get",(yourMsg: any) => {
		text.value = yourMsg
	})

	onUnmounted(() => {
		emitter.off("child1Get") //组件卸载的时候要解绑
	})

</script>
```

​	child2代码如下：

```vue
<template>
  <div class="child2">
    <h1>{{ text }}</h1>
	<input v-model="msg">
	<button @click="emitter.emit('child1Get', msg)">Send</button>
  </div>
</template>

<script setup lang="ts" name="Child2">
	import {ref,onUnmounted} from 'vue'
	import emitter from '@/utils/emitter'
	let text = ref('')
	let msg = ref('')
	
	emitter.on("child2Get",(yourMsg: any) => {
		text.value = yourMsg
	})

	onUnmounted(() => {
		emitter.off("child2Get")
	})
</script>
```

## v-model

​	在组件之间实现数据的动态绑定。

​	对于父组件比较容易，直接使用v-model然后把数据传过去就可以了，但是子组件处理的事情比较多一些。

​	首先需要使用defineProps获取父组件传过来的参数，将其显示到子组件页面上。我们先实现这一功能：

父组件如下：

```vue
<template>
	<h1>
        {{ tkydata}}
    </h1>

	<ChildComponent v-model:tkydata="tkydata"/> //这里我们把tkydata传递给子组件
</template>

<script setup lang='ts'>
	import {ref} from "vue"
    let tkydata = ref("让我自己先来写一个数据")
</script>
```

子组件如下：

```vue
<template>
	<input type="text" :value="tkydata">
</template>

<script>
	defineProps(["tkydata"])
</script>
```

​	Now, we can see the message from the father is displayed on the child component. But the data doesn't update if we change the data from the input component.

​	To handle this problem, we need use the event to trigger data updating.

We should add this code in child component:

```vue
<template>
	<input type="text" 
           :value="tkydata" 
           @input=emit("update:tkydata", (<HTMLInputElement>$event.target).value)>
</template>

<script>
	defineProps(["tkydata"])
    const emit = defineEmits(["update:tkydata"])
</script>
```

​	Read at here, you must find it is actuall use event system to achieve binding the data between the father and the child.

​	==$event has two situation==

1. if you use $event in original html mark, \$event means the html element, so you should use .target to get its object.
1.  if you use $event in mark defined by yourself, \$event is the data given by another components.

## attrs

​	This tool is used to transit data from father to grandchild, and child is a bridge.

​	When father transit its data to his child by props, but the child doesn't use "defineProps", where are these data to go?

​	The answer is in \$attrs.

​	Now assume that father give his child varibles of 'a, b, c, d' and the child get 'a';

father:

```vue
<template>
	<child v-bind={'a':a, 'b':b, 'c':c, 'd':d}/>
</template>

<script setup lang="ts">
	import {ref} from "vue"
    let a = ref(1)
    let b = ref(2)
    let c = ref(3)
    let d = ref(4)
</script>
```

child:

```vue
<script setup lang="ts">
	defineProps(["a"])
</script>
```

​	At this situation, if you open the browser development tools, you will see 'props' has 'a', and '$attrs' has 'b, c, d'.

​	==More $attrs details need to learn/==

​	what will happen if the child use props to transit \$attrs to its child, also father's grandchild?

like this:

```vue
<template>
	<grandchild v-bind="$attrs"/>
</template>
<script setup lang="ts">
	defineProps(["a"])
</script>
```

​	The grandchild can use "b, c, d" in the same way his father used.

```vue
<template>
	<h1>
        {{b}}
    </h1>
</template>

<script setup lang="ts">
	defineProps(["b", "c", "d"])
</script>
```

## $refs and \$parent

​	\$refs is used to transit data from father to child and $parent reversed.

​	Beforing use $refs, we can use ref in father to get its children's component for data seperately.

Father :

```vue
<template>
	<div class="father">
		<h1>My first child have a {{ childtoy }}</h1>
		<h1>My second child have a {{ childtoy2 }}</h1>
		<Child1 ref="c1" />
		<Child2 ref="c2" />
		<button @click="buttonFunction">Button</button>
	</div>
</template>

<script setup lang="ts" name="Father">
	import Child1 from './Child1.vue'
	import Child2 from './Child2.vue'
	import { ref } from "vue";

	let c1 = ref()
	let c2 = ref()
	let childtoy = ref()
	let childtoy2 = ref()

	function buttonFunction() {
		childtoy.value = c1.value['toy']
        //c1.value['toy'] = 'xxx' //that's ok, remember you shouldn't use .value
		childtoy2.value = c2.value['toy']
	}
</script>
```

​	Children should expose its data by using defineExpose;

Child1 as example:

```vue
<script setup lang="ts" name="Child1">
	import { ref } from "vue";
	// 数据
	let toy = ref('Paperpass')
	defineExpose({toy})
</script>
```

​	Ok, that's seems all right, but if father has handreds of children? Now we have a demand which is give all the children a new toy "basketball", if we achieve it as the same way upper displayed, that's too much tasks.

​	We can use \$refs in html marks as a parameter, and in functions using it.

Just like this:

```vue
<script>
	function buttonFunction(value: any) {
		for (let item in value) {
			value[item].toy += ' ' + 'basketball'
		}
	}
</script>
```

​	==Emphasize it: You should  use .value to get real value when it is a lonely ref.You shouldn't use any attribute when a ref in reactives.==

## _provide-inject

```vue 
without mid person to transit data from grandfather and grandson.

import {provide} from "vue", using it to provide data to his descendant.
import {inject} from "vue", using it to get data from father by provide.	

The default data of inject.

Provide the ability of object transit.
```

​	provide and inject allows grandfather and grandson exchange data without father, also intermediary.

```vue
<script>
import {provide} from "vue", using it to provide data to his descendant.
import {inject} from "vue", using it to get data from father by provide.
</script>
```

​	Assuming grandfather has 100 yuan, he transit it to his grandson, and his grandson take off 10 yuan.

grandfather like this:

```vue
<template>
  <div class="father">
    <h1>I have {{ coins }}</h1>
    <Child />
  </div>
</template>
<script setup lang="ts" name="Father">
    import Child from "./Child.vue";
    import {ref, provide} from "vue"
    let coins = ref(100)
    provide("coins", {value: coins, takeOff: () => {
      coins.value -= 10
    }})
</script>
```

grandson like this:

```vue
<template>
  <div class="grand-child">
    <h3>我是子组件, my grandfather has {{ coins.value }}</h3>
    <button @click="coins.takeOff">take off the 10 yuan</button>
  </div>
</template>

<script setup lang="ts" name="GrandChild"> 
  import GrandChild from './GrandChild.vue'
  import {inject} from "vue"

  let coins = inject('coins', {value: 0, takeOff: () => {}})

</script>
```

​	You can set default value at the second parameter of inject.

## slot-default

​	Assuming such a situation, we have one father component and a child model.In father component, we need set three child component, every component has different content.

​	Intuitively, we set three component by <child /> one by one and give them different content. Then using v-if, v-else-if to handle different situation in child.That's ok, but to complicated.

​	Actually, we can write child component as <> </>,between them writing the content we want child display.

Firstly, we prepare a child model:

```vue
<template>
    <div>
        <h1>{{ title }}</h1>
        <br>
        <slot></slot>
    </div>
</template>

<script setup lang="ts" name="Child">
    defineProps(["title"])
</script>
```

Father can give his child title by props and writing html view between <></>,like this:

```vue
<template>
    <div class="diswindow">
        <Child title="Game">
            <spawn>{{ gameName }}</spawn>
        </Child>
        <Child title="list">
            <ul>
                <ui v-for="item in infoList">
                    {{ item }}
                </ui>
            </ul>
        </Child>
    </div>
</template>

<script setup lang="ts" name="tkymain">
    import Child from "./Child.vue"
    import {ref, reactive} from "vue"

    let gameName = ref("MineCraft")
    let infoList = reactive(["tky got 100 grade", "tky is the most famouse swer"])
</script>
```



## slot-named

​	Sometimes, we have one more area needed to put content from father in children component, Or we want set our data in fixed area but writing none structures.At this situation, we can use named slot.

​	Just like other component, you can add an attribute in the matk, name.

```vue
<slot name="slot1"></slot>
```

```vue
<template>
    <div>
        <slot name="title"></slot>
        <br>
        <slot name="content"></slot>
    </div>
    
</template>

<script setup lang="ts" name="Child">
    defineProps(["title"])
</script>
```

​	In father, slot names are only permitted in <template> and vue component, consequently, we can use a <template> to wrap the comtent you want to display in child.

```vue
<template>
    <div class="diswindow">
        <Child>
            <template v-slot:title>
                Game
            </template>
            <template #content>
                {{ gameName }}
            </template>
        </Child>
        <Child>
            <template #title>
                List
            </template>
            <template #content>
                <ul>
                <ui v-for="item in infoList">
                    {{ item }}
                </ui>
            </ul>
            </template>
        </Child>
    </div>
</template>

<script setup lang="ts" name="tkymain">
    import Child from "./Child.vue"
    import {ref, reactive} from "vue"

    let gameName = ref("MineCraft")
    let infoList = reactive(["tky got 100 grade", "tky is the most famouse swer"])
</script>
```

​	There are two ways in <template> to assign what to display. v-slot:<slotname> and #<slotname>.

​	If you don't write a name to a slot, it also have a name.That means, if you only set one slot in child and named it. The slot can't be set in the correct area if you don't write a name in father's area.

## slot-domained

```/
	the situation of father use the data from son
	upper doc is ':', this doc is =
	assign name is as same as upper, combine the two ways, you can combine the two feature.
```

​	In last section, father just transit data to his son, doesn't process it. But how? The data is belonged to his son, not seen to his father.

​	At this situation, we should use slot-domained to pass data to his father.

​	==tips: last section, assign the name of slot is using ':', this section, using'='to get data. you can also combine the two form==

father:

```vue
<template>
    <div class="diswindow">
        <Child>
            <template v-slot:title>
                <span>This is a List</span>
            </template>
            <template v-slot:content="datas">
                <ol>
                    <li v-for="item in datas.data">{{ item }}</li>
                </ol>
            </template>
        </Child>
        <Child>
            <template v-slot:title>
                <span>This is another List</span>
            </template>
            <template v-slot:content="datas"> // this name is can be freely.
                <ul>
                    <li v-for="item in datas.data">{{ item }}</li>
                </ul>
            </template>
        </Child>
    </div>
</template>

<script setup lang="ts" name="tkymain">
    import Child from "./Child.vue"
    import {ref, reactive} from "vue"

    let gameName = ref("MineCraft")
    let infoList = reactive(["tky got 100 grade", "tky is the most famouse swer"])
</script>
```

son:

```vue
<template>
    <div>
        <slot name="title"></slot>
        <br>
        <slot name="content" :data="list"></slot>
    </div>
</template>

<script setup lang="ts" name="Child">
    import {ref, reactive} from "vue"
    defineProps(["title"])
    let list = reactive([
        'tky is good',
        'tkt is an excellent swe',
        'tky need a gentle and quiet and provide him active and supportive mood.'
    ])
</script>
```

# others api

​	In this section, we just introduce  some main other api.

## shallowRef and shallowReactive

​	shallowRef and shallow Reactive can just handle the first layer response data, that means .value are permiited to response but .value.xxx aren't permitted.

## readonly and shallowReadonly

​	You can use readonly to create a read-only variable based on a ref or reactive data.

​	If you use shallowReadonly, you will get a shallow read only variable.That's mean you can't change it in the first laryer but can in deeper layers.

## toRaw and markRow

​	toRaw allow you change a response data to a common data. It is not advice recive the return data of toRaw.

```ts
	let tky = toRaw(ref(123))
```

​	This usage is not adviced.

​	markRow will make the variable common data permanently.

## customRef

​	customRef permit you define your own reponse data.For example, you can define a response data that changed six seconds after you change it.

​	Main content: customRef need give it a function which receive two parameters.track, and trigger.In addition, you should complete get() and set()function.

​	It is advice to define your customRef in hooks.

The following is the hook:

```ts
import {customRef} from "vue"

export default function(initValue: string) {
    let rowData = initValue
    let timmer:number

    let resData = customRef((track, trigger) => {
        return {
            get() {
                track()
                return rowData
            },
            set(value) {
                clearTimeout(timmer)
                timmer = setTimeout(() => {
                    rowData = value
                    trigger()
                }, 2000);
            }
        }
    })
    return resData
}
```

​	track() is telling vue what variable need to track; tigger() is the funtion to touch off vue.

We can use it in vue component:

```vue
<template>
    <div class="diswindow">
        <div>
            <h1>{{ data }}</h1>
            <input v-model="data">
        </div>
    </div>
</template>

<script setup lang="ts" name="tkymain">
    import useTkyRef from "@/hooks/useTkyRef"
    let data = useTkyRef("what are you doing now")
</script>
```

## Teleport

​	Assuming you have two component, the first one is a outer container, the second one is the inner component. Now you want set the inner compnent in the center refering to the whole window.

​	At this time, you may use <Teleport>.

Before using:

```vue
<template>
    <div class="popwindow">
        <h1>This is the title of popwindow</h1>
        <p>
            This is the content of the popwindow;
        </p>
    </div>
</template>
```

After using:

```vue
<template>
    <Teleport to="body">
        <div class="popwindow">
            <h1>This is the title of popwindow</h1>
            <p>
                This is the content of the popwindow;
            </p>
    	</div>
    </Teleport>
    
</template>
```



# CSS

## 选择器

### 一、基础选择器 (Basic Selectors)



这些是最常见、最基础的选择器，用于直接选取元素。

- **通用选择器 (\*)**
  - **用法**: `* { ... }`
  - **功能**: 选择页面上的**所有** HTML 元素。
  - **注意**: 很少单独使用，因为它会影响所有元素，通常用于全局重置样式。
- **标签选择器 (Type Selector)**
  - **用法**: `p { ... }`
  - **功能**: 根据元素的标签名来选择所有匹配的元素，例如 `p` 会选择所有 `<p>` 标签。
  - **注意**: 适合用于设置元素的默认样式。
- **类选择器 (.class)**
  - **用法**: `.my-class { ... }`
  - **功能**: 根据元素的 `class` 属性来选择元素。一个元素可以有多个类，用空格分隔。这是最常用、最灵活的选择器。
  - **注意**: 推荐在日常开发中大量使用，因为它具有高度的复用性。
- **ID 选择器 (#id)**
  - **用法**: `#my-id { ... }`
  - **功能**: 根据元素的 `id` 属性来选择**唯一**的元素。在 HTML 页面中，`id` 属性的值必须是唯一的。
  - **注意**: 具有非常高的优先级，但由于其唯一性，不适合用于复用样式，应谨慎使用。

------



### 二、组合选择器 (Combinators)



组合选择器允许你根据元素之间的关系来选择元素，这使得选择器更加灵活和精确。

- **后代选择器 (Descendant Selector)**
  - **用法**: `div p { ... }` (用空格分隔)
  - **功能**: 选择**所有**作为 `div` 元素的后代的 `p` 元素。无论 `p` 嵌套多深，只要它在 `div` 里面，都会被选中。
- **子代选择器 (Child Selector)**
  - **用法**: `div > p { ... }`
  - **功能**: 只选择作为 `div` 元素的**直接子元素**的 `p` 元素。
  - **注意**: 比后代选择器更精确，因为它只匹配直接的父子关系。
- **相邻兄弟选择器 (Adjacent Sibling Selector)**
  - **用法**: `div + p { ... }`
  - **功能**: 只选择**紧挨着** `div` 元素的**下一个** `p` 元素。
- **通用兄弟选择器 (General Sibling Selector)**
  - **用法**: `div ~ p { ... }`
  - **功能**: 选择**所有**与 `div` 元素拥有相同父元素，并且**位于 div 之后**的 `p` 元素。

------



### 三、属性选择器 (Attribute Selectors)



属性选择器根据元素的属性及其值来选择元素。

- `[attribute]`
  - **用法**: `a[title] { ... }`
  - **功能**: 选择所有带有 `title` 属性的 `<a>` 元素。
- `[attribute="value"]`
  - **用法**: `a[href="https://example.com"] { ... }`
  - **功能**: 选择 `href` 属性值恰好为 `https://example.com` 的 `<a>` 元素。
- `[attribute^="value"]` (以...开头)
  - **用法**: `a[href^="#"] { ... }`
  - **功能**: 选择所有 `href` 属性值以 `#` 开头的 `<a>` 元素，常用于定位页面内的锚点链接。
- `[attribute$="value"]` (以...结尾)
  - **用法**: `img[src$=".png"] { ... }`
  - **功能**: 选择所有 `src` 属性值以 `.png` 结尾的 `<img>` 元素。
- `[attribute*="value"]` (包含...)
  - **用法**: `a[href*="example"] { ... }`
  - **功能**: 选择所有 `href` 属性值中包含 `example` 字符串的 `<a>` 元素。

------



### 四、伪类和伪元素 (Pseudo-classes & Pseudo-elements)



它们用于选择元素的特殊状态或某个部分，而不是元素本身。



#### 伪类 (Pseudo-classes)



伪类以**一个冒号 :** 开头，用于选择元素在特定状态下的样式。

- `:hover`: 鼠标悬停在元素上时。
- `:active`: 元素被激活（如鼠标按下）时。
- `:focus`: 元素获得焦点时（如表单输入框）。
- `:nth-child(n)`: 选择作为其父元素的第 `n` 个子元素的元素。
- `:first-child` / `:last-child`: 选择作为其父元素的第一个 / 最后一个子元素的元素。



#### 伪元素 (Pseudo-elements)



伪元素以**两个冒号 ::** 开头，用于选择元素的某个部分。

- `::before`: 在元素内容之前插入一个**虚拟**元素。
- `::after`: 在元素内容之后插入一个**虚拟**元素。
- `::first-line`: 选择元素的第一行文本。
- `::first-letter`: 选择元素的第一个字母。

------



### CSS 优先级 (Specificity)



当一个元素被多个 CSS 规则选中时，浏览器会根据**优先级（Specificity）**来决定应用哪个样式。优先级高的规则会覆盖优先级低的规则。

优先级的计算规则可以用一个**四位数**来表示：`(a, b, c, d)`。

1. **a (内联样式)**: 如果样式写在元素的 `style` 属性中，`a` 为 `1`。`a` 具有最高的优先级。
2. **b (ID 选择器)**: 选中了多少个 `ID` 选择器，`b` 就是多少。
3. **c (类、属性、伪类选择器)**: 选中了多少个类、属性或伪类选择器，`c` 就是多少。
4. **d (标签、伪元素选择器)**: 选中了多少个标签或伪元素选择器，`d` 就是多少。

**优先级比较原则**:

- 从左到右依次比较 `a`、`b`、`c`、`d` 的值，值大的优先级高。
- 如果所有值都相等，则**后定义的样式**会覆盖先定义的样式。

**!important**:

- `!important` 是一个特殊的标记，它会**强制**将某个属性的优先级提到最高，甚至高于内联样式。
- **注意**: 应当尽量避免使用 `!important`，因为它会破坏样式的级联性，让代码难以维护。



## flexbox

### 📚 Flexbox 核心概念



Flexbox (弹性盒模型) 是一种一维布局模型，专门用来在**容器内**对**项目**进行排列、对齐和分配空间。它非常适合构建各种复杂的布局，尤其是当你不确定内容的确切大小时。

- **🎯 Flex 容器 (Flex Container)**: 通过设置 `display: flex;` 或 `display: inline-flex;` 来创建的父元素。所有 Flex 布局的控制都从这里开始。
- **🎯 Flex 项目 (Flex Item)**: 容器内的直接子元素。它们就是你要排列和布局的对象。
- **💡 主轴 (Main Axis)**: Flex 项目的排列方向。由**容器**的 `flex-direction` 属性决定。
- **💡 交叉轴 (Cross Axis)**: 垂直于主轴的方向。

好的，帮你整理一份关于 CSS Flexbox 的学习笔记。这份笔记将重点突出核心概念和实用技巧，并巧妙地使用 emoji 来增强可读性和记忆点。



### 🔍 容器的属性 (Flex Container Properties)



这些属性用来控制**所有 Flex 项目的整体布局**。

- `flex-direction` **(主轴方向)**:

  - `row` (默认值): 从左到右排列。
  - `column`: 从上到下排列。
  - `row-reverse`: 从右到左排列。
  - `column-reverse`: 从下到上排列。
  - **💡 记忆点**: 记住 `row` 是水平，`column` 是垂直。

- `flex-wrap` **(换行)**:

  - `nowrap` (默认值): 不换行，项目会被压缩。
  - `wrap`: 换行，项目会从新的一行开始。
  - **🛠️ 实用场景**: 创建响应式卡片列表或导航栏时，让项目在空间不足时自动换行。

- `justify-content` **(主轴对齐)**:

  - `flex-start` / `flex-end`: 对齐主轴起点 / 终点。
  - `center`: 居中对齐。
  - `space-between`: 项目间距相等，两端没有间距。
  - `space-around`: 项目间和两端都有间距。
  - `space-evenly`: 项目间和两端间距完全相等。
  - **💡 记忆点**: 这是控制**水平**对齐的关键。

- `align-items` **(交叉轴对齐)**:

  - `flex-start` / `flex-end`: 对齐交叉轴起点 / 终点。
  - `center`: 居中对齐。
  - `stretch` (默认值): 项目被拉伸以适应容器高度。
  - **💡 记忆点**: 这是控制**垂直**对齐的关键。

- `flex-flow` **(简写)**:

  - `flex-flow: <flex-direction> <flex-wrap>;`
  - **示例**: `flex-flow: row wrap;`

  ### 🛠️ 项目的属性 (Flex Item Properties)

  

  这些属性用来控制**单个 Flex 项目的布局**。

  - `flex-grow` **(放大比例)**:
    - 默认值 `0`，表示不放大。
    - **示例**: `flex-grow: 1;` 让项目平分剩余空间。
  - `flex-shrink` **(缩小比例)**:
    - 默认值 `1`，表示当空间不足时会缩小。
    - **示例**: `flex-shrink: 0;` 禁止项目缩小。
  - `flex-basis` **(初始大小)**:
    - 定义在分配剩余空间前，项目的初始大小。优先级高于 `width`。
    - **示例**: `flex-basis: 100px;`
  - `flex` **(简写)**:
    - `flex: <flex-grow> <flex-shrink> <flex-basis>;`
    - **常用简写**:
      - `flex: 1;` 相当于 `flex: 1 1 0;` (自动占据剩余空间)
      - `flex: none;` 相当于 `flex: 0 0 auto;` (不放大不缩小，按内容尺寸)
  - `align-self` **(单个项目对齐)**:
    - 可以覆盖容器的 `align-items` 属性，让单个项目在交叉轴上进行不同的对齐。
    - **示例**: `align-self: center;` (让这个项目单独垂直居中)
  - `order` **(排序)**:
    - 默认值 `0`。
    - 可以改变项目在主轴上的排列顺序，数值越小越靠前。
    - **示例**: `order: 1;` 会让项目排在 `order: 0;` 的项目之后。

### 💡 常见应用场景与技巧



1. **水平垂直居中**

```css
.container {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
}
```

2. **两端对齐，中间留白**

```css
.container {
  display: flex;
  justify-content: space-between;
}
```

3. **多列等高布局**

- `display: flex;` 的子元素默认就会等高。这是一个非常方便的特性。

4. **固定侧边栏，内容区自适应**

```css
/* 容器 */
.container {
  display: flex;
}
/* 固定宽度的侧边栏 */
.sidebar {
  flex: none; /* 或者 flex: 0 0 200px; */
  width: 200px;
}
/* 自适应宽度的内容区 */
.content {
  flex: 1;
}
```

