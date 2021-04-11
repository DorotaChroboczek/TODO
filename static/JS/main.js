function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

var activeItem = null
var list_snapshot = []

buildList()

function buildList(){
    var wrapper = document.getElementById('list-wrapper')
    //wrapper.innerHTML = ''

    var url = 'http://127.0.0.1:8000/api/task-list/'

    fetch(url)
    .then((resp) => resp.json())
    .then(function (data){
        console.log('Data:', data)

        var user_list = data
        for (var i in user_list){

            try{
                document.getElementById(`data.row-${i}`).remove()
            }catch(err){
            }


            var title = `<span class="title">${user_list[i].title}</span>`
            if (user_list[i].complete == true){
                title = `<strike class="title">${user_list[i].title}</strike>`
            }

            var item = `
                <div id="data.row-${i}"
                class="task-wrapper flex-wrapper">
                    <div style="flex:7">
                        <span class="member">${user_list[i].member}
                        </span>
                    </div>
                    <div style="flex:7">
                        ${title}
                    </div>
                    <div style="flex:1">
                        <button class="btn btn-sm btn-outline-info edit">Edit
                        </button>
                    </div>
                    <div style="flex:1">
                        <button class="btn btn-sm btn-outline-dark delete">-
                        </button>
                    </div>
                </div>
            `
            wrapper.innerHTML += item
        }

        if (list_snapshot.length > user_list.length){
            for (var i = user_list.length; i < list_snapshot.length; i++){
                document.getElementById(`data.row-${i}`).remove()
            }
        }
        list_snapshot = user_list

        for (var i in user_list){
            var editBtn = document.getElementsByClassName('edit')[i]
            var deleteBtn = document.getElementsByClassName('delete')[i]
            var title = document.getElementsByClassName('title')[i]

            editBtn.addEventListener('click', (function (item){
                return function (){
                    editItem(item)
                }
            })(user_list[i]))

            deleteBtn.addEventListener('click', (function (item){
                return function (){
                    deleteItem(item)
                }
            })(user_list[i]))

            title.addEventListener('click', (function (item){
                return function (){
                    completeStatus(item)
                }
            })(user_list[i]))

        }
    })
}

var form = document.getElementById('form-wrapper')
form.addEventListener('submit', function(e){
    e.preventDefault()
    console.log('Form submitted')
    var url = 'http://127.0.0.1:8000/api/task-create/'
    if (activeItem != null){
        var url = `http://127.0.0.1:8000/api/task-update/${activeItem.id}/`
        activeItem = null
    }

    var member = document.getElementById('member').value
    var title = document.getElementById('title').value

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'member': member, 'title': title})
    }).then(function (response){
        buildList()
        document.getElementById('form').reset()
    })

})

function editItem(item){
    console.log('Item clicked:', item)
    activeItem = item
    document.getElementById('member').value = activeItem.member
    document.getElementById('title').value = activeItem.title
}

function deleteItem(item){
    console.log('Item deleted:', item)
    fetch(`http://127.0.0.1:8000/api/task-delete/${item.id}/`, {
        method: 'DELETE',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        }
    }).then((response) => {
        buildList()
    })
}

function completeStatus(item){
    console.log('complete clicked:', item)
    item.complete = !item.complete
    fetch(`http://127.0.0.1:8000/api/task-update/${item.id}/`, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'member': item.member, 'title': item.title, 'complete': item.complete})
    }).then((response) => {
        buildList()
    })
}
