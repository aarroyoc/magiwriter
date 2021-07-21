function main(){
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");
    ctx.strokeStyle = "red";
    ctx.lineCap = "round";
    ctx.lineWidth = 20;
    let lastPointX = null;
    let lastPointY = null;
    canvas.addEventListener("touchstart", evt => {
        lastPointX = evt.changedTouches[0].clientX-evt.target.offsetLeft;
        lastPointY = evt.changedTouches[0].clientY-evt.target.offsetTop;
        evt.preventDefault();
    });
    canvas.addEventListener("touchend", evt => {
        lastPointX = null;
        lastPointY = null;
        evt.preventDefault();
        predict();
    });
    canvas.addEventListener("touchmove", evt => {
        if(lastPointX !== null && lastPointY !== null){
            const newPointX = evt.changedTouches[0].clientX-evt.target.offsetLeft;
            const newPointY = evt.changedTouches[0].clientY-evt.target.offsetTop;
            ctx.beginPath();
            ctx.moveTo(lastPointX, lastPointY);
            ctx.lineTo(newPointX, newPointY);
            ctx.stroke();
            lastPointX = newPointX;
            lastPointY = newPointY;
            evt.preventDefault();
        }
    });
    canvas.addEventListener("mousedown", (evt) => {
        lastPointX = evt.clientX-evt.target.offsetLeft;
        lastPointY = evt.clientY-evt.target.offsetTop;
    });
    canvas.addEventListener("mouseup", () => {
        lastPointX = null;
        lastPointY = null;
        predict();
    });
    canvas.addEventListener("mousemove", (evt) => {
        if(lastPointX !== null && lastPointY !== null){
            const newPointX = evt.clientX-evt.target.offsetLeft;
            const newPointY = evt.clientY-evt.target.offsetTop;
            ctx.beginPath();
            ctx.moveTo(lastPointX, lastPointY);
            ctx.lineTo(newPointX, newPointY);
            ctx.stroke();
            lastPointX = newPointX;
            lastPointY = newPointY;
        }
    });
    document.getElementById("clear").onclick = () => {
        ctx.clearRect(0, 0, 500, 500);
    };
    function predict() {
        const svmLinear = document.getElementById("svm_linear");
        const svmRbf = document.getElementById("svm_rbf");
        const knn = document.getElementById("knn");
        const keras = document.getElementById("keras");
        //window.open(canvas.toDataURL(), "_blank");
        fetch("/api/mnist", {
            method: "POST",
            body: JSON.stringify({
                algorithm: "svm_linear",
                image: canvas.toDataURL()
            }),
            headers: {
                "Content-Type": "application/json"
            }
        }).then(res => res.json())
        .then(res => svmLinear.textContent = res.prediction);
        fetch("/api/mnist", {
            method: "POST",
            body: JSON.stringify({
                algorithm: "svm_rbf",
                image: canvas.toDataURL()
            }),
            headers: {
                "Content-Type": "application/json"
            }
        }).then(res => res.json())
        .then(res => svmRbf.textContent = res.prediction);
        fetch("/api/mnist", {
            method: "POST",
            body: JSON.stringify({
                algorithm: "knn",
                image: canvas.toDataURL()
            }),
            headers: {
                "Content-Type": "application/json"
            }
        }).then(res => res.json())
        .then(res => knn.textContent = res.prediction);

        fetch("/api/mnist", {
            method: "POST",
            body: JSON.stringify({
                algorithm: "keras",
                image: canvas.toDataURL()
            }),
            headers: {
                "Content-Type": "application/json"
            }
        }).then(res => res.json())
        .then(res => keras.textContent = res.prediction);
    };
}
main();