$(document).ready(function(){

    $('#myDropdowni').select2({
        dropdownParent: $('#addNewModal')
    });

    loadQuiztonList();

    $(document).on('click','.editQuizton', function(){
        $('#addNewModal').modal('show')
    })

    $(document).on('click','#addQuizton', function(){
        $('#addNewModal').modal('show')
    })

    function loadQuiztonList(){
        url = $('#quiztonList').data('url');
        csrf_token = $('#csrf_token').val();
        console.log(url);
        $.ajax({
            url : url,
            type: 'POST',
            data:{'csrfmiddlewaretoken':csrf_token},
            success: function(data){
                $('#quiztonList').html(data)
                $('#quizTable').DataTable();
            }
        })
    }
    // $('#addNewModal').on('shown.bs.modal', function () {
    //     $('#myDropdowni').select2({
    //         dropdownParent: $('#addNewModal')
    //     });
    // });

    $('#quizForm').on('submit', function(e){

        var classLevel = $('#classLevel').val();
        var image = $('#inputImage').val();
        var audio = $('#inputAudio').val();
        var video = $('#inputVideo').val();

        if(classLevel == ''){
            toastmessage('error', 'Class Level is mandatory')
        }
            
        e.preventDefault();
        path = $(this).data('action');
        var formData = new FormData(this);
        var csrf_token = $('#csrf_token').val();
        $.ajax({
            url : path,
            type: 'POST',
            data:  formData,
            processData: false,
            contentType: false,
            success: function (data) {
                if(data.status==200)
                {
                    loadQuiztonList();
                    toastmessage('success', data.msg)
                    $('#addNewModal').modal('hide')
                }
                else
                {
                    toastmessage('error', data.msg)
                }
            }
        })
        
        // console.log(formData);

    })
})