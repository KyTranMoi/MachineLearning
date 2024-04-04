// const puppeteer = require('puppeteer');

// (async () => {
//   // Mở trình duyệt
//   const browser = await puppeteer.launch();

//   // Mở trang web mới
//   const page = await browser.newPage();
//   await page.goto('https://shopee.vn/search?keyword=qu%E1%BA%A7n%20%C4%91%C3%B9i');

//   // Thực hiện một số thao tác, ví dụ: lấy tiêu đề trang
//   const title = await page.title();
//   console.log(`Tiêu đề trang: ${title}`);

//   // Lấy và in nội dung HTML của trang
//   const htmlContent = await page.content();
//   // console.log(`Nội dung HTML:\n${htmlContent}`);

//   // Đóng trình duyệt
//   await browser.close();
// })();
const puppeteer = require('puppeteer');

(async () => {
  // Mở trình duyệt
  const browser = await puppeteer.launch();

  // Mở trang web mới
  const page = await browser.newPage();
  await page.goto('https://shopee.vn/search?keyword=qu%E1%BA%A7n%20%C4%91%C3%B9i');

  // Thực hiện một số thao tác, ví dụ: lấy tiêu đề trang
  const title = await page.title();
  console.log(`Tiêu đề trang: ${title}`);

  // Lấy và in nội dung HTML của trang
  const htmlContent = await page.content();
  // console.log(`Nội dung HTML:\n${htmlContent}`);

  // Trích xuất thông tin từ các phần tử li
  const itemList = await page.$$('.col-xs-2-4.shopee-search-item-result__item');
  itemList.forEach(async (item) => {
    const title = await item.$eval('.yQmmFK', node => node.innerText);
    const price = await item.$eval('.WTFwws', node => node.innerText);
    console.log('Title:', title);
    console.log('Price:', price);
  });

  // Đóng trình duyệt
  await browser.close();
})();
