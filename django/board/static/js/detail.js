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
