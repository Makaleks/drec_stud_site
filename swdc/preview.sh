python gen.py
sed -e "s/{% block content %}/<section class='card'><h2>Проблемы в работе системы оплаты<\/h2><div><input id='show_5' type='checkbox' class='hidden shownews'><div class='card-maintext cutted'>Уважаемы студенты!<br>По техническим причинам (от нас не зависящих), к сожалению, в данный момент сервис пополнения счёта на сайте работает не корректно и деньги не доходят. В связи с этим настоятельно рекомендуем вам на время воздержаться от пополнения счёта. В случае экстренной необходимости, сделать это можно, написав <a href='https:\/\/vk.com\/id...'>Александру<\/a>, либо оплатить счёт на сайте наличными, обратившись к&nbsp;<a href='https:\/\/vk.com\/...'>Алексею<\/a>&nbsp;в 323 комнату.&nbsp;<br>Мы приносим свои извинения за доставленные неудобства и работаем над проблемой.<\/div><small class='text-muted'>Обновлено 17 апреля 2018, 15:18 <a href='\/?news=5'>Ссылка<\/a><\/small><\/div><\/section>/" -e "s/{% .* %}//;s/{{ STATIC_URL }}/static\//;s/{{ .* }}//" ../gen/core/templates/base.html > ../gen/preview.html
