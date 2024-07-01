// 목록으로 클릭 시 actionForm 보내기
document.querySelector("#list").addEventListener("click", (e) => {
  e.preventDefault();
  actionForm = document.querySelector("#actionForm");
  actionForm.action = "/board/";
  actionForm.submit();
});

const deleteAll = document.querySelectorAll(".delete");

deleteAll.forEach((item) => {
  item.addEventListener("click", (e) => {
    e.preventDefault();
    // href 값 가져오기
    if (confirm("정말로 삭제하겠습니까?")) {
      location.href = e.target.href;
    }
  });
});
