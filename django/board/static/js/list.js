const actionForm = document.querySelector("#actionForm");

// 제목 클릭 시 actionForm 보내기
document.querySelector("tbody").addEventListener("click", (e) => {
  e.preventDefault();

  // href 값 가져오기
  // actionForm action 수정 /board/23

  actionForm.action = `/board/${e.target.getAttribute("href")}`;
  actionForm.submit();
});

// 검색창 셀렉트에 변화가 일어나면 value 가져온 후 actionForm에 반영
document.querySelector(".so").addEventListener("change", (e) => {
  actionForm.querySelector("#so").value = e.target.value;
  actionForm.submit();
});

// 페이지 나누기 + 검색어
// 페이지 나누기 클릭시 href 에 있는 값 가져오기
// actionForm 의 page value 변경하기
document.querySelector(".pagination").addEventListener("click", (e) => {
  e.preventDefault();
  actionForm.action = "";
  actionForm.querySelector("#page").value = e.target.getAttribute("href");
  actionForm.submit();
});

document.querySelector("#btn_search").addEventListener("click", (e) => {
  // 검색어 가져오기
  const top_keyword = document.querySelector("#top_keyword").value;

  if (top_keyword == "") {
    // 없는 경우 alert()
    alert("검색어를 입력해 주세요");
    top_keyword.focus();
    return;
  }
  // 있는 경우 actionForm keyword value 에 삽입
  actionForm.querySelector("#keyword").value = top_keyword;
  actionForm.querySelector("#page").value = 1;
  actionForm.submit();
});
