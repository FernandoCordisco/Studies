var name_user = 'fernando rodrigues cordisco vilela'
var division_list = name_user.split(' ')
var name_initials = ''

function initial_collection() {

    division_list.forEach(function(word) {
        name_initials = name_initials + word[0]
    })
    return name_initials
}


name_initials = initial_collection()
console.log(name_initials.toUpperCase())