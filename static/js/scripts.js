/**
 * Function Navbar
 */
$(".nav-item").each(function (index) {
    $(this).click(function () {
        $(".nav-item").removeClass("active");
        $(this).addClass("active");
        $(".section").removeClass("active");
        $($(".section")[index]).addClass("active");
    });
});


/**
 * Function for selection or not selection nav and section
 */
let selection = '{{ selection }}'
if (selection === 'True') {
    $(".nav-item").removeClass("active")
    $(".nav-item:nth-child(4)").addClass("active")
    $(".section").removeClass("active")
    $(".section:nth-child(4)").addClass("active")
} else if (selection === 'False') {
    $(".nav-item").removeClass("active")
    $(".nav-item:nth-child(5)").addClass("active")
    $(".section").removeClass("active")
    $(".section:nth-child(5)").addClass("active")
}


/**
 * Function for display table input
 */
// $(".btn-overlay").click(function () {
//     var cls = $(".input-table").prop('classList');
//     if (cls.contains("active")) {
//         $(".input-table").removeClass("active");
//         $(this).html("DOWN &oror;");
//     } else {
//         $(".input-table").addClass("active");
//         $(this).html("UP &andand;");
//     }
// });

/**
 * Function to insert data from input to table
 */
// $(".btn-add").on("click", function () {
//     var jenis_kelamin = $("#input_jk").val();
//     var status = $("#input_status").val();
//     var usia = $("#input_usia").val();
//     var pekerjaan = $("#input_pekerjaan").val();
//     var pendapatan = $("#input_pendapatan").val();
//     var produk = $("#input_produk").val();
//     if (!jenis_kelamin || !status || !usia || !pekerjaan || !pendapatan || !produk) return
//     $("#my_table tbody:last-child").append(
//         `
//         <tr>
//             <td>${jenis_kelamin}</td>
//             <td>${status}</td>
//             <td>${usia}</td>
//             <td>${pekerjaan}</td>
//             <td>${pendapatan}</td>
//             <td>${produk}</td>
//         </tr>
//         `
//     )
//     if ($("#my_table tbody #table_null").length > 0) {
//         $("#my_table tbody #table_null").remove();
//     }
//     nullInput();
// });

/**
 * Function for reset input
 */
// function nullInput() {
//     var jenis_kelamin = $("#input_jk").val(null);
//     var status = $("#input_status").val(null);
//     var usia = $("#input_usia").val(null);
//     var pekerjaan = $("#input_pekerjaan").val(null);
//     var pendapatan = $("#input_pendapatan").val(null);
//     var produk = $("#input_produk").val(null);
// }

/**
 * Function for display sheet to table
 */
// $("#input_file").change(function (e) {
//     if ($(this).val().length > 0) {
//         var file = this.files[0]
//         var reader = new FileReader();
//         reader.readAsArrayBuffer(file)
//         reader.onload = function () {
//             var data = new Uint8Array(reader.result);
//             var workbook = XLSX.read(data, {
//                 type: 'array'
//             });
//             var first_sheet_name = workbook.SheetNames[0];
//             var worksheet = workbook.Sheets[first_sheet_name];
//             var result = XLSX.utils.sheet_to_json(worksheet, {
//                 header: 1
//             });
//             var table_output = '<table class="styled-table">';
//             for (var row = 0; row < result.length; row++) {
//                 if (row === 0){
//                     table_output += '<thead>'
//                 }else if (row === 1) {
//                     table_output += '<tbody>'
//                 }
//                 table_output += '<tr>';
//                 for (var cell = 0; cell < result[row].length; cell++) {
//                     if (row == 0) {
//                         if (result[row][cell]) {
//                             table_output += '<th>' + result[row][cell] + '</th>';
//                         }
//                     } else {
//                         if (result[row][cell] !== "") {
//                             table_output += '<td>' + result[row][cell] + '</td>';
//                         }
//                     }
//                 }
//                 table_output += '</tr>';
//                 if (row === 0){
//                     table_output += '</thead>'
//                 }else if (row === 1) {
//                     table_output += '</tbody>'
//                 }
//             }
//             table_output += '</table>';
//             $("#excel_data").html(table_output);
//         }
//         $(".no-file").css('display', 'none');
//     } else {
//         $(".no-file").css('display', 'block');
//     }
// });