$(document).ready(function(){

    $('#classTable').DataTable();

    $(document).on('click','.editClass', function(){

        var class_details = []
        $(this).closest('tr').find('td').each(function(){
            class_details.push($(this).text())
        })

        var classid = $(this).data('classid')
        $('#id_classid').val(classid)
        $('#id_addedit').val('edit')
        $('input[name="classno"]').val(class_details[1])
        $('input[name="class_level"]').val(class_details[2])
        $('input[name="class_level_abbr"]').val(class_details[3])
        $('#addNewModal').modal('show')
    })
    
    $(document).on('click','.addClass', function(){
        $('#id_addedit').val('add')
        $('input[name="classno"], input[name="class_level"],input[name="class_level_abbr"]').val('')
    })


})