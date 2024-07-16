$(document).ready(function(){

    $('#quizTable').DataTable();


    $(document).on('click','.editQuizton', function(){
        $('#addNewModal').modal('show')
    })
})