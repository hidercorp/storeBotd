# date-time format
dt_format = "%d.%m.%Y %H:%M:%S"

welcome_user = "Вас приветствует бот интернет-магазина.\n Можете приступать к покупкам!"
welcome_admin = "Приветствуем владельца! :) \n Вы можете управлять ботом здесь."
welcome_again_user = "Рады видеть вас снова! Можете приступать к покупкам!"

send_contact = "Отправить контактные данные"
contact_err = "Для завершения заказа требуются Ваши контакты..."    # Добавить "назад" (отправляем в корзину)

catalog_btn_user = "Каталог"
cart_btn_user = "Корзина"
orders_btn_user = "Заказы"
info_btn_user = "INFO"

orders_btn_admin = "Заказы"
edit_btn_admin = "Каталог"
stat_btn_admin = "Статистика"
info_btn_admin = "INFO"

next_btn = ">"
prev_btn = "<"
show_img_btn = "показать фото"
to_cart_btn = "в корзину"   # Добавить "назад" (отправляем к списку категорий)

info_admin = "Это ваш бот. \n Он поможет продавать вашу замечательную продукцию там, где ее удобно покупать любому :)"
info_user = "Вы попали в интернет-магазин товаров для горнолыжного спорта \"MountainOne\". Приветствуем! \n" \
            "Здесь вы можете выбрать и заказать горнолыжное снаряжение. \nПросто перейдите в каталог и можно начинать!"

sticker = "BQADBQADCAEAAukKyAOh-L4TGRYMcgI"

entity = "\n<b>%s</b>\n\nОписание:\n%s\n\nНаличие: %s\nЦена: %s руб."

select_category = "Выберите категорию из списка:"   # Кнопка "главное меню" !!!
select_subcategory = "Вы выбрали категорию \"%s\". Выберите подкатегорию из списка:"  # Кнопки "главное меню"  и "назад"
# К подкатегории приписать инструкцию: "используйте <>, чтобы увидеть все товары в этой категории"

first_item = "Это начало списка!"
last_item = "Это конец списка!"
not_enough_in_stock = "Большее количество заказать нельзя"

to_cart_done = "Товар добавлен в корзину"

confirm_order_btn = "Перейти к оформлению заказа"
to_cat_btn = "Назад к списку категорий"
main_menu_btn = "Главное Меню"

in_main_menu = "Вы в Главном Меню"

cart_items = "%s\nКоличество: <b>%s</b>\nЦена: <b>%s</b>\nСтоимость: <b>%s</b>"
cart_sum = "Итого выбрано товаров: %d на сумму %.2f"
empty_cart = "Корзина пока что пуста."
cart_welcome = "<b>Содержание Вашей Корзины:</b>\n" \
               "(используйте кнопки \"+1\" и \"-1\" для изменения количества товара в корзине)\n"

cart_item_inc1_btn = "+ 1"
cart_item_dec1_btn = "- 1"
cart_item_del_btn = "удалить"

cart_item_deleted = "Удалено"

cart_confirm_btn = "Подтвердить всё"
cart_decline_btn = "Удалить всё"

cart_min_q = "Минимальное количество"

ask_contact = "Пожалуйста, предоставьте Ваши контактные данные"

delivery_methods = "Выберите способ получения товара"

delivery_carrier_btn = "Доставка курьером"  # Добавить "назад" (отправляем в корзину)
delivery_pickup_btn = "Самовывоз"

delivery_addr_input = "Введите адрес доставки"  # Добавить "назад" (отправляем в корзину)
delivery_pickup_input = "Выберите пункт самовывоза"    # Добавить "назад" (отправляем в корзину)

delivery_date_input = "Введите дату доставки заказа"    # Добавить "назад" (отправляем в корзину)
delivery_time_input = "Выберите время доставки заказа"  # Добавить "назад" (отправляем в корзину)

delivery_confirmation = "Вы заказали доставку по адресу: \"%s\".\n" \
                   "Дата и время доставки заказа: %s, %s\n" \
                   "Общая сумма к оплате: %.2f"    # Добавить "главное меню

pickup_confirmation = "Ваш заказ ждет Вас в пунке самовывоза \"%s\" c 10:00 до 18:00\n" \
                      "Общая сумма к оплате: %.2f"

select_order = "Выберите заказ:"

order_info = "Состав заказа: %s\nПолная стоимость: %.2f\nСтатус заказа: %s\nПоследнее обновление статуса: %s"

no_orders = "Вы пока не сделали ни одного заказа.\n" \
            "Посмотрите наш каталог! :D"

pickup_point = ["Сокольники", "Тимирязевская", "Бутово", "Арбатская"]

order_status_received = default_order_status = "поступил в обработку"
order_status_delivery = "доставляется"
order_status_pickup = "ожидает в пункте самовывоза"
order_status_completed = "завершен"

cancel_status_input_btn = "Отменить изменение статуса"
status_input_cancelled = "Изменение статуса заказа отменено"

orders_sort = "Выберите какие заказы отобразить, пожалуйста:"

active_orders_btn = "Незавершенные"
date_orders_btn = "На дату"
archive_orders_btn = "Завершенные"

no_selected_order = "Заказы не найдены"

date_input = "Введите дату в формате <i>ДД.ММ.ГГГГ</i> (например, 26.10.2016)"

wrong_date_format = "Вы ввели некорректную дату. Правильный формат: <i>ДД.ММ.ГГГГ</i> (например, 26.10.2016).\n" \
                    "Попробуйте еще раз, пожалуйста."
wrong_time_format = "Вы ввели некорректное время. Правильный формат: <i>ЧЧ:ММ</i> (например, 16:48).\n" \
                    "Попробуйте еще раз, пожалуйста."

edit_order_status_btn = "Изменить статус"

status_prompt = "Выберите новый статус для заказа"

status_updated = "Статус заказа обновлен!"

alarm_status_updated = "Статус Вашего заказа от %s был обновлен! Новый статус: \"%s\""

stat_type = "Выберите вид статистики для отображения"
static_stat_btn = "по заказам"
dynamic_stat_btn = "по пользователям"

to_item_list_btn = "Назад к списку товаров"

pie_title = "Заказы за %s дней"

new_users_plot_title = "Новые пользователи"
