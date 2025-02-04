<template>
    <Card class="card">
        <h1>登录</h1>
        <Menu mode="horizontal" :theme="theme" active-name="1" @on-select="user_selection">
            <MenuItem name="1">
            <Icon type="ios-folder-open" />
            打开工程
            </MenuItem>
            <MenuItem name="2">
            <Icon type="ios-add-circle-outline" />
            新建工程
            </MenuItem>
        </Menu>
        <br>
        <div v-if="selectedMenu === '1'">
            <Form ref="formInline">
                <FormItem label="Select">
                    <Select v-model="formItem.select">
                        <Option value="beijing">New York</Option>
                        <Option value="shanghai">London</Option>
                        <Option value="shenzhen">Sydney</Option>
                    </Select>
                </FormItem>
            </Form>
        </div>
        <div v-if="selectedMenu === '2'">

        </div>

    </Card>
</template>

<script>
export default {
    data() {
        return {
            selectedMenu: '1',
        }
    },

}
</script>

<style>
    .card {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    text-align: center;
    top: 22rem;
    left: 50%;
    transform: translate(-50%, -50%);
    height: 30rem;
    width: 26rem;
    }

</style>