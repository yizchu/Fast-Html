document.addEventListener('DOMContentLoaded', function () {
    const dropdownItems = document.querySelectorAll('.dropdown-item');
    const dropdownButton = document.getElementById('dropdownMenuButton');

    // 默认选项设置为"个人用户"
    dropdownButton.textContent = '个人用户';

    // 绑定点击事件来更新按钮文本
    dropdownItems.forEach(item => {
        item.addEventListener('click', function () {
            // 更新按钮文本为选中的项
            dropdownButton.textContent = item.textContent;
        });
    });
});