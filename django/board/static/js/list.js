const actionForm = document.querySelector("#actionForm");

document.querySelector("#btn_search").addEventListener("click", (e) => {
  // 검색어 가져오기
  const top_keyword = document.querySelector("#top_keyword").value;

  if (top_keyword == "") {
    // 없는 경우 alert()
    alert("검색어를 입력해 주세요");
    top_keyword.focus();
    return;
  } else {
    // 있는 경우 actionForm keyword value 에 삽입
    actionForm.querySelector("#keyword").value = top_keyword;
    actionForm.querySelector("#page").value = 1;
    // actionForm.submit();
  }
});
