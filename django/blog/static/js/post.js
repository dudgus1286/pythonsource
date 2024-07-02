document.querySelector("#like").addEventListener("click", (e) => {
  // e.target : 실제 이벤트 발생 대상 => span
  // e.currentTarget : 이벤트 대상의 부모
  // post_id 가져오기
  const postId = e.currentTarget.dataset.post;
  fetch(`/blog/post/like/${postId}`)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      if (data.is_liked) {
        document.querySelector(".like").classList.add("show");
        document.querySelector(".dislike").classList.remove("show");
      } else {
        document.querySelector(".like").classList.remove("show");
        document.querySelector(".dislike").classList.add("show");
      }

      document.querySelector(".like-total span").innerHTML = data.likes;
    });
});
