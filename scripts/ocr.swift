// Taranmış PDF -> metin (macOS Vision). Kullanım: swift scripts/ocr.swift girdi.pdf > cikti.txt
// Resmî Gazete'de yayımlanan ilke kararları görüntü olarak tarandığı için gerekir.
import Foundation
import PDFKit
import Vision

guard CommandLine.arguments.count > 1, let doc = PDFDocument(url: URL(fileURLWithPath: CommandLine.arguments[1])) else {
    FileHandle.standardError.write("PDF açılamadı\n".data(using: .utf8)!)
    exit(1)
}
for i in 0..<doc.pageCount {
    guard let page = doc.page(at: i) else { continue }
    let b = page.bounds(for: .mediaBox)
    let olcek: CGFloat = 3.0
    let w = Int(b.width * olcek), h = Int(b.height * olcek)
    guard let ctx = CGContext(data: nil, width: w, height: h, bitsPerComponent: 8, bytesPerRow: 0,
                              space: CGColorSpaceCreateDeviceRGB(),
                              bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue) else { continue }
    ctx.setFillColor(CGColor(red: 1, green: 1, blue: 1, alpha: 1))
    ctx.fill(CGRect(x: 0, y: 0, width: w, height: h))
    ctx.scaleBy(x: olcek, y: olcek)
    page.draw(with: .mediaBox, to: ctx)
    guard let img = ctx.makeImage() else { continue }
    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.recognitionLanguages = ["tr-TR"]
    req.usesLanguageCorrection = true
    try? VNImageRequestHandler(cgImage: img, options: [:]).perform([req])
    let satirlar = (req.results ?? []).compactMap { $0.topCandidates(1).first?.string }
    print("--- sayfa \(i + 1) ---")
    print(satirlar.joined(separator: "\n"))
}
