
let vm = new Vue({
    el: "#app",
    data: {
        "title": "",
        "file": ""
    },
    mounted: async function set_data() {
        const data = await eel.set_data()();

        this.title = data["title"];
    },
    methods: {
        generator_picture: async function () {
            const qrcode = document.getElementById("qrcode").value;
            // const up_text = document.getElementById("up-text").value;
            const down_text = document.getElementById("down-text").value;
            // const left_text = document.getElementById("left-text").value;
            // const right_text = document.getElementById("right-text").value;

            if (!qrcode){
                alert("網址或文字欄位不能為空值");
                return 
            }

            // const file = await eel.generator_picture(qrcode, up_text, down_text, left_text, right_text)();
            const file = await eel.generator_picture(qrcode, down_text)();

            this.file = file;
        }
    }
})

eel.expose(show_message);
function show_message(msg) {
    alert(msg);
}